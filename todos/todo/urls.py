from django.urls import path
from . import views


urlpatterns = [
    #path("", views.home, name="home"),
    # This is a class-based view. 
    # We need to call the as_view() method to convert it into a view function 
    # that can be used in the URL patterns.
    path("", views.HomeView.as_view(), name="home"),
    path("add/", views.AddView.as_view(), name="add_todo"),
]
