from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from posts.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "posts/home.html", {"posts": posts, "username": "uday"})

def list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginurl"))
    
    posts = Post.objects.all()
    return render(request, "posts/list.html", {"posts": posts, "username": "uday"})

def post(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginurl"))
    
    # try:
    #     post = Post.objects.filter(id=id).first()
    # except Post.DoesNotExist:
    #     raise Http404("Post not found")
    post = get_object_or_404(Post, id=id)
    
    return render(request, 'posts/post.html', {"post" : post})
    
def google(request):
    return HttpResponseRedirect('https://www.google.com') 

def redirect(request, id):
    url = reverse("posturl", args=[id]) 
          
    return HttpResponseRedirect(url)

def getglobal(request):
    return render(request, 'global.html')

def set(request):
    response = HttpResponse("Set")
    response.set_cookie("name", "uday", max_age=5, httponly=True)
    response.set_cookie("theme", "dark")

    return response

def get(reuest):
    theme = reuest.COOKIES.get("theme")
    name = reuest.COOKIES.get("name")

    return HttpResponse(f"Theme: {theme}, <br> Name: {name}")

def delete(request):
    response = HttpResponse("Delete")
    response.delete_cookie("name")
    response.delete_cookie("theme")

    return response

def set_with_render(request):
    print("Set the view with render")
    response = render(request, 'posts/set_with_render.html')
    response.set_cookie("name", "uday", max_age=5, httponly=True)
    response.set_cookie("theme", "dark")

    return response

def exception(request):
    raise Exception("This is an exception")

def template_response(request):
    return TemplateResponse(request, 'posts/template_response.html', {})
