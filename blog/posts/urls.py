from django.urls import path

#from posts import views
from . import views # if we aare in the same folder then we can use dot ' . '

urlpatterns = [
    #path("list/", views.list, name="allposturl"),
    path("list/", views.PostListView.as_view(), name="allposturl"),
    #path("<int:id>/", views.PostDetailView.as_view(), name="posturl"), # here, int: is a path convertor
    path("<int:id>/", views.PostDetailView.as_view(), name="posturl"), # here, int: is a path convertor
    path("tags/<int:id>/", views.tags, name="tagsurl"), # here, int: is a path convertor
    #path("search/", views.search, name="searchpostsurl"),
    path("search/", views.SearchView.as_view(), name="searchpostsurl"),
    path("global/", views.getglobal),
    path("set/", views.set),
    path("set-with-render/", views.set_with_render),
    path("get/", views.get),
    path("delete/", views.delete),
    path("exception", views.exception),
    path("template-response", views.template_response),
]