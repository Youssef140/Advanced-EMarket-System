from django.contrib import admin
#imporitng the Product model
from .models import Product,Category,UserSearchedImage
#Registration and Customization of the admin stuff for the listings app
from django.contrib import admin


#customizatio of how products are displayed in the admin page
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','category','price','in_stock','list_date','admin')
    #specifying which fields can be clicked to be updated
    list_display_links = ('id','title')
    #enables filtering by admins
    list_filter = ('admin',)
    #allows the is_published checkmark to be pressed directly
    list_editable = ('is_published',)
    #searching based on given fields
    #for foreign keys the __name is the name of the field we would like to search with from the FK table
    search_fields = ('title','category__name')
    list_per_page = 25



#registering the Product model in order for the admin to see it
admin.site.register(Product,ListingAdmin)
admin.site.register(Category)
admin.site.register(UserSearchedImage)





currency_choices = (
    ('usd', 'USD'),
    ('lbp', 'LBP')
)

