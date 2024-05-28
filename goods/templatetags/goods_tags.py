from goods.models import Categories
from django import template
from django.utils.http import urlencode


register = template.Library()

@register.simple_tag()
def tags_category():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    querry = context["request"].GET.dict()
    querry.update(kwargs)
    return urlencode(querry)