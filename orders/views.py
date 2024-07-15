from django.db import transaction
from django.shortcuts import render
from orders.forms import OrderCreatedForm


# Create your views here.
def create_order(request):
    if request.method == "POST":
        form = OrderCreatedForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    ...







    
        
        else:
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,

            }
            form = OrderCreatedForm(initial=initial)

        context={
            "title":"Оформление заказа",
            "form": form,
        }

    return render(request, "orders/create_order.html", context)
