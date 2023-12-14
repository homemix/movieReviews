from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from movie.models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


@login_required
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    data = {
        "movie": movie,
        "reviews": reviews
    }
    return render(request, 'detail.html', data)

@login_required
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('detail', review.movie.id)
        else:
            errors = form.errors
            data = {
                'errors': errors,
                'movie': movie,
                'form': ReviewForm()
            }
            return render(request, 'create_review.html', data)
    else:
        data = {
            "movie": movie,
            "form": ReviewForm()
        }
        return render(request, 'create_review.html', data)

@login_required
def update_review(request, review_id):
    review = get_object_or_404(
        Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'update_review.html',
                      {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request,
                          'update_review.html',
                          {'review': review, 'form': form, 'error': 'Bad data in form'})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)


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
