from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="registerurl"),
    path("login/", views.auth_login, name="loginurl"),
    path("logout/", views.auth_logout, name="logouturl"),
]