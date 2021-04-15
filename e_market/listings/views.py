from django.db.models import Q
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
    queryset_list = Product.objects.order_by('-list_date')

    if('keywords' in request.GET):
        keywords = request.GET['keywords']
        if(keywords):
            # queryset_list = queryset_list.filter(title__icontains = keywords)
            queryset_list = queryset_list.filter(Q(brand_name__icontains=keywords)
                                                 | Q(title__icontains=keywords)
                                                 | Q(category__name__icontains=keywords)).distinct()

    context = {
        'products' : queryset_list,
        'values' : request.GET
    }

    return render(request, 'listings/search.html',context)


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
    current_cat = Category.objects.all().filter(id = category_id)

    context = {
        'categories': categories,
        'current_cat': current_cat
    }
    print(context.get('current_cat'))
    return render(request,'listings/category.html',context)



def offers(request):
    return render(request, 'listings/offers.html')


def offer(request):
    return render(request, 'listings/offer.html')

def cart(request):
    return render(request, 'listings/cart.html')

def checkout(request):
    return render(request, 'listings/checkout.html')
