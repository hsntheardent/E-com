from django.shortcuts import render
from storeproduct.models import Product
def home(request):
#homepage pr product show krwain gy jo manually add kiay hain admin page pr through storeproduct, query run krain gay
    #query
    products = Product.objects.all().filter(is_available=True)#is_available=True      # sirf available products
    context = { 
        'products': products,
    }
    # our html page : our DB store data
    # context purpose : fetch data from DB to render on html page
    return render(request,'home.html',context) 