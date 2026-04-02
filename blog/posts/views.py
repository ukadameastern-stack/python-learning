from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from .forms import CommentForm
from django.db.models import Q
from posts.models import Post, Tag
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "posts/home.html", {"posts": posts})

def list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginurl"))
    
    posts = Post.objects.all().order_by("-id")
    paginator = Paginator(posts, 3, orphans=2)  # Show 2 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, "posts/list.html", {"posts": posts})

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"
    paginate_by = 3
    paginate_orphans = 2
    ordering = ["-id"]

    login_url = "loginurl"          # URL name
    redirect_field_name = "next"    # optional (default is 'next')

def post(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginurl"))
    
    # try:
    #     post = Post.objects.filter(id=id).first()
    # except Post.DoesNotExist:
    #     raise Http404("Post not found")
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # commit=False means that we want to create a Comment object but 
            # not save it to the database yet

            comment = form.save(commit=False)
            comment.post = post
            comment.comment_author = request.user 
            comment.save()
            post_url = reverse("posturl", args=[id])

            return redirect(post_url, id=id)
    else:
        form = CommentForm()
    
    return render(request, 'posts/post.html', {"post" : post, "form": form})

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "posts/post.html"
    context_object_name = "post"
    pk_url_kwarg = "id"   # important (since you're using id)

    # GET request
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    # POST request (form submit)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()   # get Post instance
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.comment_author = request.user
            comment.save()

            return redirect("posturl", id=self.object.id)

        # if form invalid → re-render page with errors
        context = self.get_context_data()
        context["form"] = form
        
        return self.render_to_response(context)

def tags(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginurl"))
    
    tag = Tag.objects.filter(id=id).first()
    if not tag:
        raise Http404("Tag not found")

    return render(request, 'posts/tags.html', {"tags": tag.post_set.all(), "tag": tag})   

def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginurl"))
    
    query = request.GET.get("q", None)
    posts = Post.objects.filter(
        Q(post_title__icontains=query) | 
        Q(post_content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    paginator = Paginator(posts, 3, orphans=2)  # Show 2 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(
        request, 
        'posts/search.html', 
        {
            "posts": posts, 
            "query": query,
            "total_results": posts.paginator.count
        }
    )

class SearchView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/search.html"
    context_object_name = "posts"
    paginate_by = 3
    paginate_orphans = 2

    # 🔍 core logic
    def get_queryset(self):
        query = self.request.GET.get("q", None)

        if query:
            return Post.objects.filter(
                Q(post_title__icontains=query) |
                Q(post_content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct().order_by("-id")

        return Post.objects.none()  # no query → no results

    # 📦 extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")

        context["query"] = query
        if context.get("page_obj"):
            context["total_results"] = context["page_obj"].paginator.count
        else:
            context["total_results"] = 0
        print("Context:", context)

        return context

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
