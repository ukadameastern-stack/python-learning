from django.urls import path

#from posts import views
from . import views # if we aare in the same folder then we can use dot ' . '

urlpatterns = [
    path("list/", views.list, name="allposturl"),
    path("<int:id>/", views.post, name="posturl"), # here, int: is a path convertor
    path("global/", views.getglobal),
    path("set/", views.set),
    path("set-with-render/", views.set_with_render),
    path("get/", views.get),
    path("delete/", views.delete),
    path("exception", views.exception),
    path("template-response", views.template_response),
]