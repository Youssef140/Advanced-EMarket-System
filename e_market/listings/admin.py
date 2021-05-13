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
    list_filter = ('admin','list_date','is_offer',)
    #allows the is_published checkmark to be pressed directly
    list_editable = ('is_published','in_stock')
    #searching based on given fields
    #for foreign keys the __name is the name of the field we would like to search with from the FK table
    search_fields = ('category__name','title','brand_name',)
    list_per_page = 20

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent_categ_id','photo_main','is_child','is_parent','description')
    #specifying which fields can be clicked to be updated
    list_display_links = ('id',)
    #enables filtering by admins
    # list_filter = ('admin',)
    #allows the is_published checkmark to be pressed directly
    list_editable = ('is_child',)
    #searching based on given fields
    #for foreign keys the __name is the name of the field we would like to search with from the FK table
    search_fields = ('name','id')
    list_per_page = 10



#registering the Product model in order for the admin to see it
admin.site.register(Product,ListingAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(UserSearchedImage)




currency_choices = (
    ('usd', 'USD'),
    ('lbp', 'LBP')
)
