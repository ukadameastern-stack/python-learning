from django.urls import path

#from posts import views
from . import views # if we aare in the same folder then we can use dot ' . '

urlpatterns = [
    path("home/", views.home, name="homeurl"),
    path("<int:id>/", views.post, name="posturl"), # here, int: is a path convertor
    path("global/", views.getglobal),
]