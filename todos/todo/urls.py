from django.urls import path
from . import views
from django.views.generic.base import TemplateView # view class for class based views(2.1.1)

urlpatterns = [
    #path("", views.home, name="home"),
    # This is a class-based view. 
    # We need to call the as_view() method to convert it into a view function 
    # that can be used in the URL patterns.
    path("", views.HomeView.as_view(), name="home"),
    path("add/", views.AddView.as_view(), name="add_todo"),

    # path("about/", TemplateView.as_view(template_name="todo/about.html"  ), name="about"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("about/<str:name>/", views.AboutView.as_view(), name="about_name"),
]
