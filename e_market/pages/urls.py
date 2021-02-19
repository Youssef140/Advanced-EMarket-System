from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),#root path,name is a name that will allow us to reference this path through it
    path('about',views.about,name='about'),
]