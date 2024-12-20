
from django.views.generic import TemplateView, CreateView
from main.forms import FeedBackForm
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Главная"
        context["content"] = "Магазин мебели HOME"

        return context


# def index(request):

#     context = {
#         "title": "Home - Главная",
#         "content": "Магазин мебели HOME",

#     }
#     return render(request, "main/index.html", context)


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - о нас"

        return context


# def about(request):
#     context = {
#         "title": "Home - о нас",
#         "content": "Страница о магазине",
#         "text_on_page": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, qui.",
#     }
#     return render(request, "main/about.html", context)


class DeliveryAndPayment(TemplateView):
    template_name = "main/delivery_and_payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        delivery = self.request.GET.get("mail_or_courier")
        context["delivery"] = delivery
        context["title"] = "Home - Доставка и оплата"

        return context


class SelfPickUpPage(TemplateView):
    template_name = "main/self_pick_up.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Самовывоз"

        return context


class Contacts(CreateView):
    template_name = "main/contacts.html"
    form_class = FeedBackForm
    success_url = reverse_lazy("main:index")

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Контакты"
        return context


    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Обратный звонок заказан")
        return super().form_valid(form)
