from ast import mod
from types import NoneType
from django.db import models
from users.models import User
from goods.models import Products


class OrderItemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(order_item.products_price() for order_item in self)

    def total_quantity(self):
        if self:
            return sum(order_item.quantity for order_item in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_DEFAULT,
        verbose_name="Пользователь",
        default=None,  # попробовать сюда добавить "Удален" что бы при удалении за место NoneType было это и не было бага
        blank=True,
        null=True,
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания заказа"
    )
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    requires_delivery = models.BooleanField(
        default=False, verbose_name="Требуеться доставка"
    )
    delivery_adress = models.TextField(
        blank=True, null=True, verbose_name="Адрес доставки"
    )
    payment_on_get = models.BooleanField(
        default=False, verbose_name="Оплата при получении"
    )
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(
        max_length=50, default="В обработке", verbose_name="Статус заказа"
    )

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering="id",

    def __str__(self):
        if isinstance(self.user, NoneType):
            return f"Заказ № {self.pk}| Покупатель Удален-Удален"

        return f"Заказ № {self.pk} | Покупатель {self.user.first_name}-{self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(
        to=Products,
        on_delete=models.SET_DEFAULT,
        verbose_name="Продукт",
        null=True,
        default=None,
    )
    name = models.CharField(max_length=50, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количнство")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата продажи"
    )
    objects = OrderItemQuerySet.as_manager()

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"
        ordering="id",
        

    def products_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self) -> str:
        return f"Товар {self.product.name} | Заказ № {self.order.pk}"
