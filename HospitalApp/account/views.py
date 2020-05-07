from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def signup(request):
    """
    Basic user registration
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
        return render(request, 'account/signup.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'account/signup.html', {'form': form})


def sign_in(request):
    """
    Login form
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
        else:
            form = AuthenticationForm()
            return render(request, 'account/signin.html', {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, 'account/signin.html', {"form": form})


def log_out(request):
    """Logout the user"""
    logout(request)
    return redirect('homepage')