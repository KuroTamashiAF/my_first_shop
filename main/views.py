from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories

# Create your views here.


def index(request):
    categories = Categories.objects.all()

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - о нас",
        "content": "Страница о магазине",
        "text_on_page": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, qui.",
    }
    return render(request, "main/about.html", context)
