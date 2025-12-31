from django.contrib import admin
from .models import Category
# Register your models here.

# hum category main product name add krain to category slup auto generate ho jaye
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')
     
admin.site.register(Category,CategoryAdmin)


    