from django.shortcuts import render,get_list_or_404
from goods.models import Products


# Create your views here.
def catalog(request, category_slug):
    "контроллер каталога"

    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "title": "Home - каталог",
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    "контроллер продукта"
    product = Products.objects.get(slug=product_slug)

    context = {"product": product}
    return render(request, "goods/product.html", context)
