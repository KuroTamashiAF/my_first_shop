"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from carts.views import CartAddView, CartChangeView, CartRemoveView

app_name = "carts"


urlpatterns = [
    path("cart_add/", CartAddView.as_view(), name="cart_add"),
    path("cart_change/", CartChangeView.as_view(), name="cart_change"),
    path("cart_remove/", CartRemoveView.as_view(), name="cart_remove"),
]
