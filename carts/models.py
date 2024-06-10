from django.db import models
from users.models import User
from goods.models import Products

# Create your models here.


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, verbose_name="Товар"
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления"
    )
    session_key = models.CharField(max_length=32, blank=True, null=True)

    objects = CartQuerySet().as_manager()

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
        db_table = "cart"

    def __str__(self):
        return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)