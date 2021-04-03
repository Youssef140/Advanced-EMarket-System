from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='listings'),#root path,name is a name that will allow us to reference this path through it
    path('<int:product_id>',views.listing,name='product'),
    path('search', views.search, name='search'),
]