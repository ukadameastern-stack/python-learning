from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # view class for class based views(2.1.1)
from django.views.generic import TemplateView # (2.1.2)
from django.views.generic import RedirectView # (2.1.3)
from django.views.generic import ListView # (2.1.1.1)
from .forms import TodoForm
from todo.models import Todo
from django.shortcuts import redirect


# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")

# Class based view (2.1.1)
# class HomeView(View):
#     def get(self, request):
#         todos = Todo.objects.all()
#         #return HttpResponse("Hello, World! This is a class-based view.")
#         return render(request, "todo/index.html", {"todos": todos})

class HomeView(ListView):
    model = Todo
    ordering = ["-id"] # This will order the todos by id in descending order. 
    # The latest added todo will be shown at the top of the list. 
    # If we want to order it in ascending order, we can use "id" instead of "-id".

    #template_name = "todo/index.html" # By default, 
    # ListView will look for a template named "todo/todo_list.html" 
    # (app_name/model_name_list.html). 
    # If we want to use a different template name, 
    # we can specify it using the template_name attribute.

    #context_object_name = "todos" # This is the name of the variable 
    # that will be used in the template to access the list of todos.
    # By default, it would be "object_list", but we are changing it 
    # to "todos" for better readability in the template.

    # def get_queryset(self):
    #     return Todo.objects.filter(todo__icontains="buy")
    #     # This will filter the todos that contain the word "buy" in the todo field.
    #     # We can also use other filters like startswith, endswith, exact, etc.
     
    
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

    