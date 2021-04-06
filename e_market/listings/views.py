from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def index(request):

    products = Product.objects.all()

    paginator = Paginator(products, 3)
    page = request.GET.get('page')

    paged_products = paginator.get_page(page)

    context = {
        'products' : paged_products
    }

    return render(request, 'listings/listings.html', context)


def listing(request, product_id):
    products = Product.objects.all()

    for prd in products:
        if prd.id == product_id:
            product = prd

    context = {
        'product': product
    }
    return render(request, 'listings/listing.html',context)


def search(request):
    return render(request, 'listings/search.html')
