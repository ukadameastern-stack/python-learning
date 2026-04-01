from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # view class for class based views(2.1.1)
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
    