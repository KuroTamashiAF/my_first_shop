from carts.models import Cart
from django import template


register = template.Library()


@register.simple_tag()
def user_carts(request):    
    "  a,jhbfkhbzkghv "
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)