from django.shortcuts import render
from goods.models import Products


# Create your views here.
def catalog(request):
    "контроллер каталога"
    goods = Products.objects.all()

    context = {
        "title": "Home - каталог",
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    "контроллер продукта"
    context = {}
    return render(request, "goods/product.html", context)
