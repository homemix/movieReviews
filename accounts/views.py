from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def sign_up_account(request):
    data = {
        "form": UserCreationForm,
    }
    return render(request, 'signup_account.html', data)
