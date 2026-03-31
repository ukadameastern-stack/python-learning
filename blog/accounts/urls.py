from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="registerurl"),
    path("login/", views.auth_login, name="loginurl"),
    path("logout/", views.auth_logout, name="logouturl"),
]


#Django built in authentication views for login and logout
# from django.urls import path
# from . import views
# from .forms import LoginForm
# from django.contrib.auth.views import LoginView, LogoutView

# urlpatterns = [
#     path("register/", views.register, name="registerurl"),
#     #Django built in authentication views for login and logout
#     path(
#         "login/", 
#         LoginView.as_view(
#             template_name="accounts/login.html", 
#             authentication_form=LoginForm
#         ), 
#         name="loginurl"
#     ),
#     path("logout/", LogoutView.as_view(), name="logouturl"),
# ]