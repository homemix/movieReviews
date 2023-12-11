from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    search_term = request.GET.get('search_movie')
    data = {'name': 'kennedy wambua', 'age': 30, 'search_term': search_term}

    return render(request, 'home.html', data)


def about(request):
    return HttpResponse("Welcome to about page")


def signup(request):
    subscription_email = request.GET.get('subscription_email')
    return render(request, 'signup.html', {'subscription_email': subscription_email})
