from django.db import IntegrityError
from .tasks import send_booking_webhook, send_email

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
import django_rq
from django_rq import get_queue
from .models import Campsite
from .serializers import CampsiteSerializer, RegisterSerializer, BookingSerializer
from .pagination import CustomPagination
from .validators import OverlapValidator
from .dataclasses import BookingInput, PaymentDetails 
from .models import Booking

class JobsFinishedAPI(APIView):
    def get(self, request):
        
        return Response({
            "jobs": {
                "webhooks": self.get_jobs("webhooks"),
                "emails": self.get_jobs("emails")
            }
        })    
    
    def get_jobs(self, quueue_name):
        queue = get_queue(quueue_name)
        finished_jobs = queue.finished_job_registry.get_job_ids()

        job_data = []
        for job_id in finished_jobs:
            job = queue.fetch_job(job_id)
            job_data.append({
                "id": job.id,
                "enqueued_at": job.enqueued_at.isoformat() if job.enqueued_at else None,
                "result": str(job.result)[:100]
            })

        return job_data
    
class JobsFailedAPI(APIView):
    def get(self, request):
        queue = get_queue("webhooks")
        failed_jobs = queue.failed_job_registry.get_job_ids()

        job_data = []
        for job_id in failed_jobs:
            job = queue.fetch_job(job_id)
            job_data.append({
                "id": job.id,
                "enqueued_at": job.enqueued_at.isoformat() if job.enqueued_at else None,
                #"failed_at": job.failed_at.isoformat() if job.failed_at else None,
                "result": str(job.result)[:100]
            })

        return Response({"failed_jobs": job_data})
    
class ExecuteJobAPI(APIView):
    def post(self, request):
        booking_id = request.data.get("booking_id")

        if not booking_id:
            return Response({"error": "booking_id is required."}, status=400)

        queue = get_queue("webhooks")
        job = queue.enqueue(send_booking_webhook, booking_id)

        return Response({
            "job_id": job.id,
            "status": job.get_status(),
            "booking_id": booking_id
        })

class JobsWaitingAPI(APIView):
    def get(self, request):
        queue = get_queue("webhooks")
        jobs = queue.jobs

        webhook_job_data = []
        for job in jobs:
            webhook_job_data.append({
                "id": job.id,
                "status": job.get_status(),
                "enqueued_at": job.enqueued_at.isoformat() if job.enqueued_at else None,
                "result": str(job.result)[:100]
            })

        queue = get_queue("emails")
        jobs = queue.jobs

        email_job_data = []
        for job in jobs:
            email_job_data.append({
                "id": job.id,
                "status": job.get_status(),
                "enqueued_at": job.enqueued_at.isoformat() if job.enqueued_at else None,
                "result": str(job.result)[:100]
            })

        return Response({
            "jobs": {
                "webhooks": webhook_job_data,
                "emails": email_job_data
            }
        })    

class CampsiteListAPI(ListAPIView):
    queryset = Campsite.objects.all()
    serializer_class = CampsiteSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        # enqueue job: Just for testing
        if request.query_params.get("enqueue_webhook") == "true":
            send_booking_webhook.delay(str("fffd8990-bcd7-400c-b30a-1aaae4066383"))
            django_rq.enqueue(send_email, request.user.id, queue="emails")

        return super().list(request, *args, **kwargs)



class BookingListAPI(ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class RegisterAPI(CreateAPIView):
    serializer_class = RegisterSerializer


class BookingCreateAPI(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        data = serializer.validated_data

        payment_data = data.get("payment_details")

        payment_details = (
            PaymentDetails(**payment_data)
            if payment_data else None
        )

        # dataclass instance
        booking_input = BookingInput(
            campsite=data["campsite"].id,
            start_date=data["start_date"],
            end_date=data["end_date"],
            guests=data["guests"],
            provider_id=data["provider_id"],
            provider_booking_id=data["provider_booking_id"],
            user=self.request.user.id,
            payment_details=payment_details
        )

        # dataclass to validator
        validator = OverlapValidator()
        error = validator.validate(booking_input)

        if error:
            raise ValidationError(error)

        try:

            # ✅ Save booking
            booking = serializer.save(user=self.request.user)

            # ✅ Enqueue webhook AFTER success
            send_booking_webhook.delay(str(booking.id))

        except IntegrityError as e:
            error_msg = str(e)

            if "prevent_overlapping_bookings" in error_msg:
                raise ValidationError({
                    "error": "This campsite is already booked for the selected dates."
                })

            elif "unique_provider_booking" in error_msg:
                raise ValidationError({
                    "error": "This provider booking already exists.",
                    "details": {
                        "provider_id": serializer.validated_data.get("provider_id"),
                        "provider_booking_id": serializer.validated_data.get("provider_booking_id")
                    }
                })

            else:
                raise ValidationError({
                    "error": "Database constraint error."
                })
        
            