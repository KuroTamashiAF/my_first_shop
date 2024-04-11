from django.shortcuts import render


# Create your views here.
def catalog(request):
    "контроллер каталога"

    context = {}

    return render(request, "goods/catalog.html", context)


def product(request):
    "контроллер продукта"
    context = {} 
    return render(request, "goods/product.html", context)
