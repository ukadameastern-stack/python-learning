from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # view class for class based views(2.1.1)
from django.views.generic import TemplateView # (2.1.2)
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
        print(kwargs)
        context["message"] = f"This is the about page for {kwargs['name']}. Message from the AboutView class. Class extends TemplateView and overrides the get_context_data method to add a message to the context that will be passed to the template. The template can then display this message using the {{ message }} variable."
        return context

    