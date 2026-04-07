# tasks.py
import datetime
import json
from django_rq import job


def webhook_failure_handler(job, connection, type, value, traceback):
    print(f"[WEBHOOK ERROR] Job {job.id} failed: {value}")


@job("webhooks", on_failure=webhook_failure_handler)
def send_booking_webhook(booking_id):
    # Just to test webhook_failure_handler
    #raise Exception("Simulated webhook failure") 

    timestamp = datetime.datetime.utcnow().isoformat()

    payload = {
        "event": "booking.created",
        "booking_id": str(booking_id),
        "timestamp": timestamp,
        "data": {
            "status": "confirmed",
            "source": "booking-api"
        }
    }

    print("=== WEBHOOK JOB EXECUTED ===")
    print("Booking ID:", booking_id)
    print("Timestamp:", timestamp)
    print("Payload:", json.dumps(payload, indent=2))

    # simulate failure (optional test)
    # raise Exception("Simulated webhook failure")

def send_email(user_id):
    print("sending email", user_id)    