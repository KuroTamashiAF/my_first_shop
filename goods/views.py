from typing import Any
from urllib import request
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView
from goods.models import Products
from goods.utils import q_search


# Create your views here.
class CatalogView(ListView):
    model = Products
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3
    # allow_empty = False      # при пустом QuerySet будет ошибка

    def get_queryset(self) -> QuerySet[Any]:
        category_slug = self.kwargs.get("category_slug")
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if category_slug == "all":
            goods = super().get_queryset()

        elif query:
                goods = q_search(query)

        else:
            goods = super().get_queryset().filter(category__slug=category_slug)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        return goods

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["slug_url"] = self.kwargs.get("category_slug")
        return context


# def catalog(request, category_slug=None):
#     "контроллер каталога"

#     page = request.GET.get("page", 1)
#     on_sale = request.GET.get("on_sale", None)
#     order_by = request.GET.get("order_by", None)
#     query = request.GET.get("q", None)

#     if category_slug == "all":
#         goods = Products.objects.all()
#     elif query:
#         goods = q_search(query)

#     else:
#         goods = Products.objects.filter(category__slug=category_slug)
#         if not goods.exists():
#             raise Http404()

#     if on_sale:
#         goods = goods.filter(discount__gt=0)

#     if order_by and order_by != "default":
#         goods = goods.order_by(order_by)

#     paginator = Paginator(goods, 3)
#     current_page = paginator.page(int(page))

#     context = {
#         "title": "Home - каталог",
#         "goods": current_page,
#         "slug_url": category_slug,
#     }

#     return render(request, "goods/catalog.html", context)


class ProductView(DetailView):

    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name

        return context


# def product(request, product_slug):
#     "контроллер продукта"
#     product = Products.objects.get(slug=product_slug)

#     context = {"product": product}
#     return render(request, "goods/product.html", context)
