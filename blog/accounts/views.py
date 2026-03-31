
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from accounts.forms import RegisterForm, LoginForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("homeurl"))

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "User created successfully")

            return redirect(reverse("loginurl"))  # no reverse needed
        else:
            return render(request, "accounts/register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "accounts/register.html", {"form": form})   

def auth_login(request):
    messages.info(request, "")

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")

        return redirect(reverse("homeurl"))
    
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)    

            messages.success(request, "Login successful")

            return redirect(reverse("homeurl"))
        else:
            return render(request, "accounts/login.html", {"form": form})

    form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def auth_logout(request):    
    logout(request) 
    messages.success(request, "You have been logged out successfully")   
    
    return redirect(reverse("loginurl"))
