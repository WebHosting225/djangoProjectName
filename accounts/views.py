from django.shortcuts import render, redirect
from django.contrib.auth import login as login_, authenticate, logout as logout_, get_user_model
from . import forms


def dashboard(request):
    return render(request, "accounts/dashboard.html", {"title": "Dash Board"})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        form = forms.CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login_(request, user)
            return redirect("home")
    else:
        form = forms.CustomUserLoginForm()
    return render(request, "accounts/login.html", {"title": "Login", "form": form})


def logout(request):
    logout_(request)
    return redirect('home')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            display_name = form.cleaned_data.get('display_name')
            get_user_model().objects.create_user(username=username, email=email, password=password, display_name=display_name)
            user = authenticate(request, username=username, email=email, password=password, display_name=display_name)
            login_(request, user)
            return redirect("home")
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"title": "Signup", "form": form})
