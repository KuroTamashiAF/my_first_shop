from django.urls import path
from main.views import IndexView, AboutView, DeliveryAndPayment, SelfPickUpPage, Contacts

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("delivery_and_payment/", DeliveryAndPayment.as_view(), name="delivery_and_payment"),
    path("self_pickup/", SelfPickUpPage.as_view(), name="self_pickup"),
    path("contacts/",Contacts.as_view(), name="contacts"),

]
