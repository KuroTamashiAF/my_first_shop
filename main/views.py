from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    siubvuib = 0
    return render(request, "main/index.html", context={"siubvuib": siubvuib})


def about(request):
    return HttpResponse("about page")
