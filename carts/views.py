from django.shortcuts import render,redirect, HttpResponse , get_object_or_404
from .models import Cart, CartItem 
from storeproduct.models import Product
from django.core.exceptions import ObjectDoesNotExist
# Create your views here. 
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
        
        
        
def add_cart(request, product_id): # we are going to add product that we write product_id
    product = Product.objects.get(id=product_id) # get the product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request) ) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request) 
        )
        cart.save()
        # when we want to put the product inside the cart and it will becomes cart Item and in 1 cart maybe there will be multiple Item(products) 
        # in Cart so we want to combine the product and cart so will get the cartitem
    try:
            cart_item = CartItem.objects.get(product=product, cart=cart) # this will bring us th e caritem
            cart_item.quantity += 1               # cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
    except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart ,
            )   
            cart_item.save() 
            # return user to the cartpage
    return redirect('cart')    
        
        
        
         
        
def cart(request, total=0 , quantity = 0, card_item = None):
    try:
        cart = Cart.objects.get(cart_id =_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass         
    
    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
    }
    return render(request,'store/cart.html', context)





def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request)) #get tje cart
    product = get_object_or_404(Product,  id = product_id)#also get product
    cart_item = CartItem.objects.get(product=product , cart =  cart)
    if cart_item.quantity  >  1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()    
    return redirect('cart')



def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,  id = product_id)
    cart_item = CartItem.objects.get(product=product ,  cart= cart)
    cart_item.delete()
    return redirect('cart')
    