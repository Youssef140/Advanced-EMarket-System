from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout', views.logout, name='logout'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('editPassword', views.editPassword, name='editPassword'),
    path('dashboard', views.dashboard, name='dashboard'),
]