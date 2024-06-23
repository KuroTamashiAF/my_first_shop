from carts.models import Cart
from django import template
from carts.utils import get_user_carts


register = template.Library()


@register.simple_tag()
def user_carts(request):    
    "  a,jhbfkhbzkghv "
    return get_user_carts(request)