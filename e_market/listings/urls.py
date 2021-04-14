from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>',views.index,name='listings'),#root path,name is a name that will allow us to reference this path through it
    path('listing/<int:product_id>',views.listing,name='listing'),
    path('search', views.search, name='search'),
    path('categories', views.categories, name='categories'),
    path('category/<int:category_id>', views.category, name='category'),
    path('bestSellers', views.bestSellers, name='bestSellers'),
    path('offers', views.offers, name='offers'),
    path('offer', views.offer, name='offer'),

]