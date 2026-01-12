# project <> greatlart
# app <> category       # storeproduct <> store
# create virtual env
    python3 -m venv .venv
# activate
    source .venv/bin/activate        
# deactivate
    deactivate
# install django
    pip install django


# django-admin startproject project .         
also create views.py in project 
then also in mkdir static folder paste all files css,fonts,js, images         
# python manage.py collectstatic           
#       yh command is liay run krty hain yh all static files ko new static folder main paste kr dyta hai
project ki sari static files (CSS, JS, images, fonts) ko ikatha (collect) karke ek hi static/ folder me copy kar deta hai.Media (photo)  and static css fonts etc sab ko apnny project mai. aplly krna hai.

# home.html
# create base.html

# create app
django-admin startapp app
work in models.py and register the model

# pillow 
#    pip install pillow
    Pillow Python ki ek library hai jo image processing ke liye use hoti hai—jaise images ko open, edit (resize/crop), format convert, text/logo add, aur AI/ML ke liye preprocess karna.

# python manage.py makemgrations
run migrations files
# python manage.py migrate

# python manage.py runserver

# db.sqlite q delete krna parta hai?
 Django pehle se default user model bana chuka hota hai
Jab aap project bana lete ho aur migrate command chalate ho (even pehli baar), to Django default User model ka structure database me bana deta hai.


# custom user model             purpose of this hum username and password ki bajye email and password sy login krain gy


# accounts/admin.ppy

 ###### python .\manage.py createsuperuser
Email: ehteshamhassan353@gmail.com
Username: admin
First name: ehtesham
Last name: hassan  
password: 125521raja


## list_display_links= ('email','first_name','last_name')
    admin panel mein users ki information-list hoti hai,to normally sirf email ya username par click karne se user ka detail page khulta hai.lakin hum chahaty hian kh in fields pr b click krain to 'first_name','last_name' tab hi user ka data visible ho
    Aur jab aap in me se kisi bhi cheez par click karoge, to us user ka pura detailed profile page khul jayega.
# ordering = ('-date_joined',)
Default Django queries mein result ko ek order mein dikhana hota hai.
 users join hone ke date ke descending order mein aayein, yani sabse naya user pehle.  

## list filter                      
list_filter = ()Jab aap admin panel me user list dekhte ho,
toh side me filter options dikhte hain — jaise: 
✅ Active users dikhana 
👑 Admin users dikhana 
Yeh filter admin ko asaani deta hai users ko chhantne (filter) ke liye.



### fieldsets    
fieldsets = () likhne se admin panel ka layout simple ho jata hai, aur password field chhoti (minimized) dikhti hai.
fieldsets = ()#password koi b ni dekh sky ga--password aisa tha(pbkdf2_sha256$10AN5seavO39474fg8zTsyG7DxmJAA=) after aisa ho gaya

# Prepopulate Category Slug auto slug creating when we are write category in db 

# install sqlite studio
q k db.sqlite main data readable form main  ni hota is liay hum sqlite studio install kr rahay hain

# create storeproduct app
models.py  , admin.py register
auto slug create
add products manually in DB
# display products on homepage 
projrct views.py
home.html main loops run then product name  , product price , product.url
# for store html button , click on button then going on store page
create url.py
        first path in main project level directory in project url then in storeproduct url.py
then in views.py just render template  for store button
after 
# display product on store page
        products = Product.objects.all().filter(is_available=True)
         product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
# (Products by Category)is kay baad url banana hai srf specfic catory ka like this # bring the slug here for http://127.0.0.1:8000/store/shirts/   //urls.py
urls.py
views.py for slug

# context_processor.py in app.    details in .md 
# display category on store page
store.html main category link's banaye and all products ka linnk banaya/navbar,html mian all products ka link banaya

#### PRODUCT  detail page and MAKE template
storeproduct url and  views 26 simple for jsut render new temp / create template / 
 
###  SInglr Product View  
views.py 27 / droduct.html 27 , 30 ,19 / jab url search krna hai to srf product ka name aur us ka slug

### get url for product
storeproduct models 17 / home.html 37//  "store" click buton set kia on navbar.html 53  // esi trhna logo ko b home url dia // "See all" button  ko b url dia on home.html // phir es kay bad store page pr jab product kay name ya image pr click krain to us ko product page pr jana chaiay to store.html 132 137

### out of stock tab
product_detail.html  77 to 81
{% else %} 
		<a href="#" class="btn  btn-success"> <span class="text">Added to cart</span> <i class="fasfa-check"></i>  </a>
			{% endif %}
### cartapp and template
set temp simple
### Cart and CartItem model creating 
models.py 

### Add to Cart logic (On Button "Add to cart")
sab sy phly product ko add krna in "add to cart"
def _cart_id(request):   def add_cart(request):
final step apply add_cart view function here --> product_fetail.html 88 /

### getting carditem quanity
def cart
we need total , need information , need quantity as futher as well  44 sy 57

### implementing cart item 
cart.html 33 to 68     // models.py  19

### calulating tax and total
views.py 50  and 59  cart.html 78 and 82

### cart increment and decrement 
views .py  68 // urls.py path // cart.html  49

### remove_cart_item 
views.py  81 // urls.py  // cart.html 65

### handling empty card
cart.html 13 loop 13---103

### fix add-to-cart links on store 
store.html  143  
and cart page pr product name click krny sy  product open ho jaye {{ cart_item.product.get_url }}  line 39

# product already in cart
agar product already cart hai to us ko add-to-carat button show ni krwana "view-cart" show krwana hai.  store views.py Add line 29 and 34 then product.html changes from line 79
add new logic 
				{% if in_cart %}
				<a href="#" class="btn  btn-success"> <span class="text">Added to cart</span> <i class="fas fa-check"></i>  </a>
				<a href="{% url 'store' %}" class="btn  btn-outline-primary"> <span class="text">view Cart</span> <i class="fas fa-eye"></i>  </a>
		 		{% else %} 

### cart counterf on NAvbar
# basically hum cart-icon pr real cart pproduct ki count shoow krtea raha hain. 
new file . context_processor.py
def counter
setting > 'tempplates' > 'carts.context_processor.counter', on 71
navbar.html 76 then 74  

# View Details Button (Product Detail Page)