from django.urls import path
from main.views import IndexView, AboutView, DeliveryAndPayment

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("delivery_and_payment/", DeliveryAndPayment.as_view() , name="delivery_and_payment"),

]
