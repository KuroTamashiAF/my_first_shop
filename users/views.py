from django.shortcuts import render


def login(request):
    context = {
        "title": "Магазин мебели Home - Авторизация",
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
