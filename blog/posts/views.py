from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404

from posts.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "posts/home.html", {"posts": posts, "username": "uday"})

def post(request, id):
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
