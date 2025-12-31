from django.urls import path
from . import views
urlpatterns = [
    path('',views.storeproduct, name='store'),
    path('<slug:category_slug>/',views.storeproduct,name='products_by_category'), # view only shirts::url-->http://127.0.0.1:8000/store/shirts/
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),
]
 