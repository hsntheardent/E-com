from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):  
    category_name = models.CharField(max_length=50, unique=True)  
    slug = models.SlugField(max_length=100, unique=True)    # admin.py :: purpose write slug auto
    description = models.TextField(max_length=255)
    cat_image = models.ImageField(upload_to= 'photos/categories', blank=True)
                                            #'photos/categories'   ---> backend pr is tarteeb main image upload ho gi
    
    class Meta:#Category ko admin-panal main save krty hain to  django default name categorys save krta hai instead-of 
        # is ko categories likhka hona chaiay , 
        # is liay hum is name ko change krny ki koshih krty hian into categories
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
            return reverse('products_by_category', args=[self.slug] )
                        #   'products_by_category' in urls.py from storeproduct 
#Ye function category ke liye URL generate karta hai,DB se aane wale category ko uske page ka link deta hai
#.      very good explain in .md  
    def __str__(self):
        return self.category_name 