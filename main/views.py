from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    change = 1

    aura = "BOOK"
    return render(request, "main/index.html", {"cook": aura,
                                               "change": change, })


def about(request):
    return HttpResponse("about page")
