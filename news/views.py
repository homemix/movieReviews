from django.shortcuts import render

from .models import News


def news(request):
    news_list = News.objects.all()
    data = {
        "news_list": news_list
    }
    return render(request, "news.html", data)
