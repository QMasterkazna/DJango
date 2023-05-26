from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm
from .forms import LoginForm

# Create your views here.

def index(requests):
    return render(requests, 'main/main.html')

def firstlesson(requests):
    return render(requests, 'main/first_lesson.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return render(request, 'main/main.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            form = LoginForm()
            return render(request, 'main/login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'main/login.html', {'form': form})

def logout_user(requests):
    logout(requests)
    return render(requests, 'main/main.html')
