from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0

    # Do not count for admin pages
    if 'admin' in request.path:
        return {}

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))   # get single cart
        cart_items = CartItem.objects.filter(cart=cart)

        for item in cart_items:
            cart_count += item.quantity   # make sure your field name is quantity

    except Cart.DoesNotExist:
        cart_count = 0

    return dict(cart_count=cart_count)
 