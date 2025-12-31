from django.shortcuts import render,get_object_or_404
from .models import Product
from app.models import Category
from carts.models import CartItem
from carts.views import _cart_id
def storeproduct(request,category_slug=None): # bring the slug here for http://127.0.0.1:8000/store/shirts/   //urls.py
    categories = None       # yeh variables define kar rahe hain abhi, 
    products  = None        # taake aage overwrite ya use kar sakein based on condition
    if category_slug!= None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category=categories,is_available=True)  # (is_available=True) → wo products fetch honge.
        product_count = products.count()
    else:    
  #query
        products = Product.objects.all().filter(is_available=True)
#product_count sy hum products count kr skty hain` << include store.html line 121****
        product_count = products.count() # store page ki products count kr ky print kry ga on store page
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html',context)



def product_detail(request, category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,                                
    }
    return render(request,'store/product_detail.html', context) 