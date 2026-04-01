from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # view class for class based views(2.1.1)
from django.views.generic import TemplateView # (2.1.2)
from django.views.generic import RedirectView # (2.1.3)
from .forms import TodoForm
from todo.models import Todo
from django.shortcuts import redirect


# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")

# Class based view (2.1.1)
class HomeView(View):
    def get(self, request):
        todos = Todo.objects.all()
        #return HttpResponse("Hello, World! This is a class-based view.")
        return render(request, "todo/index.html", {"todos": todos})
    
class AddView(View):
    def get(self, request):
        form = TodoForm()
        return render(request, "todo/add.html", {"form": form})    
    
    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        
        return render(request, "todo/add.html", {"form": form})

class AboutView(TemplateView):
    template_name = "todo/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = kwargs.get("name", "unknown")
        context["message"] = f"This is the about page for {name}. Message from the AboutView class. Class extends TemplateView and overrides the get_context_data method to add a message to the context that will be passed to the template. The template can then display this message using the {{ message }} variable."
        return context
    
class RedirectToAboutView(RedirectView):
    #url = "/about/" # This is hardcoding the url. If we change the url pattern in urls.py, we need to change it here as well. This is not flexible and maintainable.
    pattern_name = "about_url" # this is using the route name defined in urls.py instead of hardcoding the url. This is more flexible and maintainable. If we change the url pattern in urls.py, we don't need to change it here.   
    query_string = True # This will preserve the query string parameters when redirecting. For example, if we access /about-redirect/?name=John, it will redirect to /about/?name=John and the name parameter will be preserved in the redirected URL.

    