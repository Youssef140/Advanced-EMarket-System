from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:category_id>',views.index,name='listings'),#root path,name is a name that will allow us to reference this path through it
    path('listing/<int:product_id>',views.listing,name='listing'),
    path('search', views.search, name='search'),
    path('categories', views.categories, name='categories'),
    path('category/<int:category_id>', views.category, name='category'),
    path('bestSellers', views.bestSellers, name='bestSellers'),
    path('offers', views.offers, name='offers'),
    path('offers/offer/<int:offer_id>', views.offer, name='offer'),
    path('update_item', views.update_item, name='update_item'),
    path('searchimage', views.search_image, name='search_image'),
] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

