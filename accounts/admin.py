from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

# yh es lia kia ja ra hai ta kh koi superadmin ka passwrod just read only not for edit 
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name', 'username','last_login','date_joined','is_active')
    list_display_links= ('email','first_name','last_name')# commands/86
    ordering = ('-date_joined',) #commands/89
    
    filter_horizontal =()
    list_filter = () #commands93
    fieldsets = () #commands/103
admin.site.register(Account,AccountAdmin) 