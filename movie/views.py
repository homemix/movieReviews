from django.http import HttpResponse
from django.shortcuts import render

from movie.models import Movie


def home(request):
    search_term = request.GET.get('search_movie')
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    data = {'name': 'kennedy wambua',
            'age': 30,
            'search_term': search_term,
            'movies': movies}

    return render(request, 'home.html', data)


def about(request):
    return HttpResponse("Welcome to about page")


def signup(request):
    subscription_email = request.GET.get('subscription_email')
    return render(request, 'signup.html', {'subscription_email': subscription_email})
