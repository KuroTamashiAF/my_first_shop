from django.shortcuts import redirect, render
from orders.forms import OrderCreatedForm
from users.models import User
from carts.models import Cart
from orders.models import Order, OrderItem
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError


# Create your views here.
def create_order(request):
    if request.method == "POST":
        form = OrderCreatedForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    carts_items = Cart.objects.filter(user=user)

                    if carts_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            requires_delivery=form.cleaned_data["requires_delivery"],
                            delivery_adress=form.cleaned_data["delivery_adress"],
                            payment_on_get=form.cleaned_data["payment_on_get"],
                        )
                        #   Создать заказанные товары
                        for cart_item in carts_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(
                                    f"Недостаточное количнство товара {name} на складе\
                                                        в наличии {product.quantity}"
                                )
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # очистить корзину пользователя
                        carts_items.delete()

                        messages.success(request, "Заказ оформлен")
                        return redirect("user:profile")
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect("orders:create_order")

    else:
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }

        form = OrderCreatedForm(initial=initial)

    context = {
        "title": "Оформление заказа",
        "form": form,
    }

    return render(request, "orders/create_order.html", context)
