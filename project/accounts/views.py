from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import UserRegisterForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Your account has been created! Welcome, {user.username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')
