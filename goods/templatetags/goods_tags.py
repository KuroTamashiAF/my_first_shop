from goods.models import Categories
from django import template


register = template.Library()

@register.simple_tag()
def tags_category():
    return Categories.objects.all()