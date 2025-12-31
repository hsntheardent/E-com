from django.db import models
from django.contrib.auth.models import AbstractBaseUser#hum custom user banate hain,to hum decide karte hain ke kaun kaun si fields zaroori hongi.
from django.contrib.auth.models import BaseUserManager# user create krny main help krta hia
# Create your models here.



# creating user
#MyAccountManager ek custom manager hai jo batata hai kh "User kis tarah create kiya jaye"
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name,username, email, password=None ):#self manager claass ko mention krti hai by default
        if not email:
            raise ValueError('User must have an Email address')
            
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(
            email = self.normalize_email(email),#(normalize_email)if u enter any Capital letter in email addres it will just make as a small letter
            username = username,
            first_name = first_name,
            last_name = last_name,
        )    
        
        user.set_password(password) # password ko hash karke store karta hai (plain text nahi).
        user.save(using=self._db)
        return user 
    

    # for createsuperuser (admin panel aur poore system pe access rakhta hai.) and admin + staff
    def create_superuser(self, first_name, last_name,username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password= password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active =True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    



                ### 
#Django by default ek User model deta hai (usme username, password, etc. hota hai)  
# Lekin agar hum apna custom User model banana hai (jisme email login ke liye use ho, 
#  extra fields ho jaise phone_number), to hum AbstractBaseUser ko inherit karte ho.   
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)  
    
    #  Auto created fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)#login par update ho.
    is_admin = models.BooleanField(default=False)#agar user admin hai to us ko admin power hasil ho gi, agar user normal hai to
    is_staff = models.BooleanField(default=False)                                      #adminpower ni mily gi
    is_active = models.BooleanField(default=False)                                     
    is_superadmin = models.BooleanField(default=False)      #Superadmin boss hai jo poori company ko chalata hai.


    #jab hum python manage.py createsuper user run krty hain to django yh 2 filed must demand krta hai,  required_fields
    # hum khud add kr rhay hain createsuperuser main
    USERNAME_FIELD = 'email'#Username ki jagah email + password se login hoga
    REQUIRED_FIELDS = ['username','first_name', 'last_name'] #
    
    objects = MyAccountManager()
                                # why we write this bcz objects is the default model manager in Django. 
                                #"Use my custom manager (MyAccountManager) instead of the default objects manager."
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):# yh custom user model main must likhna hota hai
        return self.is_admin   # Agar user admin hai to sab permissions milegi.
     
    def has_module_perms(self, add_label):
        return True  # Ye batata hai ki user ko har Django app access hai (agar admin hai).
    

    ### in setting.py  AUTH_USER_MODEL = 'accounts.Account'