from django.shortcuts import render
from users.forms import UserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Магазин мебели Home - Авторизация",
        "form": form,
    }
    return render(request, "users/login.html", context)


def registration(request):
    context = {
        "title": "Магазин мебели Home - Регистрация",
    }
    return render(request, "users/registration.html", context)


def profile(request):
    context = {
        "title": "Магазин мебели Home - Кабинет",
    }
    return render(request, "users/profile.html", context)


def logout(request):
    context = {
        "title": "Магазин мебели Home - Выход",
    }
    return render(request, "", context)