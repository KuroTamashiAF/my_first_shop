from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from main.forms import FeedBackForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from main.forms import FeedBackForm


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
        context["content"] = "Страница о магазине"
        context["text_on_page"] = (
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, qui."
        )
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


def contacts(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)

        if form.is_valid():

            name = request.POST.get("name")
            phone = request.POST.get("phone_number")

            print(name)
            print(phone)

            # return reverse_lazy("main:contacts")
    else:
        form = FeedBackForm()

    return render(request, "main/contacts.html", {"form": form})


# class ContactInformation(CreateView):
#     template_name = "main/contact_information.html"
#     form_class = FeedBackForm
#     success_url = reverse_lazy("main:index")
#     model = FeedBackCall


#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Home - Контактная информация"
#         return context

#     def form_valid(self, form):
#         name = self.request.POST.get("name")


#         print(name)
#         print("TRUE")
#         return reverse_lazy(self.success_url)
