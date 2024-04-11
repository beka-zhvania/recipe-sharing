from django.shortcuts import render, redirect
from . import views
from .forms import CustomRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            # login the user after successful registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('base:index')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipe:carousel')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('base:index')