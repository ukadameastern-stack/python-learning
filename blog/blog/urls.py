"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("post/helloworld", views.helloWorld),
    path("post/", include('posts.urls')),
    path("session/", include('sessiontut.urls')),
    path("google/", views.google), # Redirect t 3rd party URL
    path("<int:id>/", views.redirect), # Redrect to own application URL
]

admin.site.site_header = "My Blog"
admin.site.site_title = "My Blog Portal"
admin.site.index_title = "Welcome to My Blog Portal"
