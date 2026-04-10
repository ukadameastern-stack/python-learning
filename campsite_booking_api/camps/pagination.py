from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    Custom pagination class for API responses.

    Provides configurable page size with reasonable defaults for campsite listings.
    """
    page_size = 10  # Default page size
    page_size_query_param = "page_size"
    max_page_size = 100  # Maximum allowed page size