from django.contrib import admin
#imporitng the Admin model
from .models import Admin
#Registration and Customization of the admin stuff for the listings app

#registering the Product model in order for the admin to see it
admin.site.register(Admin)