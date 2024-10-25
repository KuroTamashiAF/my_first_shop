from django.db import models

# Create your models here.
class FeedBackCall(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя абонента")
    phone_number = models.CharField(max_length=15)
