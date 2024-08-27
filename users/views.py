from urllib import request
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.db.models import Prefetch, QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProFileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from carts.models import Cart
from orders.models import Order, OrderItem
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.mixins import CacheMixin


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    # success_url = reverse_lazy("main:index")

    def get_success_url(self) -> str:
        redirect_page = self.request.POST.get("next", None)
        if redirect_page and redirect_page != reverse("user:logout"):
            return redirect_page

        return reverse_lazy("main:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин мебели Home - Авторизация"
        return context

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()
        if user:
            auth.login(self.request, user)
            if session_key:
                fogot_cart = Cart.objects.filter(user=user)
                if fogot_cart.exists():
                    fogot_cart.delete()
                Cart.objects.filter(session_key=session_key).update(user=user)
                messages.success(self.request, f"{user.username}, вы вошли в аккаунт")

                return HttpResponseRedirect(self.get_success_url())


# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = auth.authenticate(username=username, password=password)
#             session_key = request.session.session_key

#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f"{username} успешно вошли в аккаунт")

#                 if session_key:
#                     # delete old authorized user carts
#                     fogot_carts = Cart.objects.filter(user=user)
#                     if fogot_carts.exists():
#                         fogot_carts.delete()
#                      # add new authorized user carts from anonimous session
#                     Cart.objects.filter(session_key=session_key).update(user=user)

#                 redirect_page = request.POST.get("next", None)
#                 if redirect_page and redirect_page != reverse("user:logout"):
#                     return HttpResponseRedirect(request.POST.get("next"))

#                 return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserLoginForm()

#     context = {
#         "title": "Магазин мебели Home - Авторизация",
#         "form": form,
#     }
#     return render(request, "users/login.html", context)


class UserRegistrationView(CreateView):
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("main:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Регистрация"
        return context

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(
            self.request,
            f"{user.username}, вы успешно зарегистрировались и вошли в аккаунт",
        )
        return HttpResponseRedirect(self.success_url)


# def registration(request):

#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             session_key = request.session.session_key
#             user = form.instance
#             auth.login(request, user)

#             if session_key:
#                 Cart.objects.filter(session_key=session_key).update(user=user)

#             messages.success(
#                 request,
#                 f"{user.username} вы успешно зарегистрировались и вошли в аккаунт",
#             )
#             return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserRegistrationForm()

#     context = {
#         "title": "Магазин мебели Home - Регистрация",
#         "form": form,
#     }
#     return render(request, "users/registration.html", context)


class UserProfileView(LoginRequiredMixin, CacheMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = UserProFileForm
    success_url = reverse_lazy("user:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Профайл успешно обновлен")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Произошла ошибка")

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - личный кабинет"
        orders = (
            Order.objects.filter(user=self.request.user)
            .prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id")
        )

        context["orders"] = self.set_get_cache(orders, f"user_{self.request.user.id}_orders", 60)
        

        return context


# @login_required
# def profile(request):
#     if request.method == "POST":
#         form = UserProFileForm(
#             data=request.POST, instance=request.user, files=request.FILES
#         )
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Профайл успешно изменен")
#             return HttpResponseRedirect(reverse("user:profile"))
#     else:
#         form = UserProFileForm(instance=request.user)

#     orders = (
#         Order.objects.filter(user=request.user)
#         .prefetch_related(
#             Prefetch(
#                 "orderitem_set",
#                 queryset=OrderItem.objects.select_related("product"),
#             )
#         )
#         .order_by("-id")
#     )

#     context = {
#         "title": "Магазин мебели Home - Кабинет",
#         "form": form,
#         "orders": orders,
#     }
#     return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect("main:index")


class UserCartsView(TemplateView):
    template_name = "users/users_cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Корзина"
        return context


# def users_cart(request):

#     context = {}
#     return render(request, "users/users_cart.html", context)
