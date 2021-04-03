from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Category

def index(request):
    categories = Category.objects.all()

    context = {
        'categories' : categories
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')

