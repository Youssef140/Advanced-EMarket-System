from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category


def index(request,category_id):
    products = Product.objects.all().filter(category=category_id)

    paginator = Paginator(products, 3)
    page = request.GET.get('page')

    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products
    }

    return render(request, 'listings/listings.html', context)


def listing(request, product_id):
    product = Product.objects.all().filter(id = product_id)

    context = {
        'product': product
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }

    return render(request, 'listings/categories.html',context)


def bestSellers(request):
    return render(request, 'listings/bestSellers.html')

def category(request, category_id):
    categories = Category.objects.all().filter(parent_categ_id = category_id)

    context = {
        'categories': categories
    }
    return render(request,'listings/category.html',context)
