from django.shortcuts import render
from django.template import context


# Create your views here.
def create_order(request):
    context = {}
    return render(request, "orders/create_order.html", context)
