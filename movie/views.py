from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. Welcome to homepage")


def about(request):
    return HttpResponse("Welcome to about page")
