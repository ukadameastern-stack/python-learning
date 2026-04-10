"""
URL configuration for campsite_booking_api project.

This module defines the main URL routing for the Django application.
It routes requests to appropriate views and includes API documentation endpoints.

Main URL patterns:
- /admin/ : Django admin interface (superuser only)
- /api/ : Application API endpoints (includes camps app URLs)
- /api/schema/ : OpenAPI schema endpoint (JSON format)
- /api/schema/swagger-ui/ : Interactive Swagger UI documentation
- /api/schema/redoc/ : Interactive ReDoc documentation

For more information on URL configuration, see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

# Import admin site from Django - provides built-in admin interface
from django.contrib import admin

# Import path() for URL routing and include() for including app-specific URLconfs
from django.urls import path, include

# Import API documentation views from drf-spectacular
# SpectacularAPIView: Generates OpenAPI schema in JSON format
# SpectacularSwaggerView: Provides interactive Swagger UI for API testing
# SpectacularRedocView: Provides alternative ReDoc documentation interface
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Main URL patterns list - defines all routes for the application
urlpatterns = [
    # Django admin interface
    # Route: /admin/
    # Purpose: Access Django admin panel for database management
    # Access: Requires superuser credentials
    path("admin/", admin.site.urls),
    
    # Include all URLs from camps application
    # Route: /api/
    # Purpose: Includes all API endpoints defined in camps/urls.py
    # Endpoints: /api/campsites, /api/register/, /api/token/, /api/bookings/, etc.
    path("api/", include("camps.urls")),
    
    # OpenAPI Schema Endpoint
    # Route: /api/schema/
    # Purpose: Serves the raw OpenAPI schema in JSON format
    # Usage: Used by Swagger UI and other API documentation tools
    # Access: No authentication required
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    # Swagger UI Interactive Documentation
    # Route: /api/schema/swagger-ui/
    # Purpose: Provides interactive, web-based API documentation
    # Features: Test endpoints directly from browser, view request/response examples
    # Access: No authentication required
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    
    # ReDoc Alternative Documentation
    # Route: /api/schema/redoc/
    # Purpose: Alternative API documentation viewer (ReDoc style)
    # Features: Clean, 3-column layout for better readability
    # Access: No authentication required
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
