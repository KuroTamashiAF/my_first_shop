
from django.db import models


# Create your models here.
class FeedBackCall(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя абонента")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    time_created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    status = models.BooleanField(verbose_name="Отметка о выполнении", default=False)

    def __str__(self):

        return f"Обратный звонок абоненту {self.name.upper()} по номеру {self.phone_number} "

    class Meta:
        verbose_name = "Обратный звонок"
        verbose_name_plural = "Обратные звонки"
        ordering = ["-time_created"]
