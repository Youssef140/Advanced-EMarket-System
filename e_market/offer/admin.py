from django.contrib import admin
from .models import Offer
from .models import Offer_Product
# Register your models here.

class OfferProductInline(admin.TabularInline):
    model = Offer_Product


class OfferAdmin(admin.ModelAdmin):
    inlines = [
        OfferProductInline,
    ]
    list_display = ('id', 'name', 'description', 'price', 'currency', 'from_date', 'to_date')

    # specifying which fields can be clicked to be updated
    list_display_links = ('id', 'name')


admin.site.register(Offer,OfferAdmin)


