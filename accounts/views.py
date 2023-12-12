from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserCreateForm


def sign_up_account(request):
    data = {
        "form": UserCreateForm,
    }
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                data = {
                    "form": UserCreateForm,
                    "error": "User already registered"
                }
                return render(request, 'signup_account.html', data)
        else:
            data = {
                'error': 'Passwords do not match',
                'form': UserCreateForm
            }
            return render(request, 'signup_account.html', data)
    else:
        return render(request, 'signup_account.html', data)


def login_account(request):
    if request.method == 'GET':
        return render(request, 'login_account.html',
                      {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'login_account.html',
                          {'form': AuthenticationForm,
                           'error': 'username and password do not match'})
        else:
            login(request, user)
            return redirect('home')


def logout_account(request):
    logout(request)
    return redirect('home')
