import json

from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Product, Category,ProductsReview
from django.http import JsonResponse
from orders.models import Order,OrderItem
from .forms import SearchImageForm, SubmitReviewForm
from .ImageSearch import LogoDetection
from django.contrib.auth.models import User
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *





def index(request,category_id):
    products = Product.objects.all().filter(category=category_id,in_stock=True)


    paginator = Paginator(products, 3)
    page = request.GET.get('page')

    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products
    }

    return render(request, 'listings/listings.html', context)


def listing(request, product_id):
    product = Product.objects.all().filter(id=product_id)
    reviews = ProductsReview.objects.all().filter(product=product_id)
    client = RecombeeClient('e-market-dev', 'S1HpoVU0JuxtjU9ewtvSnAUQh4qgKHTjr2DFbQ30LoADU2S27OsleTi1C23TNVEm')
    current_user = request.user
    if(current_user.is_authenticated):
        print("auth")
        r = AddDetailView(current_user.id, product_id, cascade_create=True)
        client.send(r)

    recommended = client.send(RecommendItemsToItem(product_id,current_user.id,5))
    print(f"Related products: {recommended}")
    context = {
        'product': product,
        'reviews':reviews,
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Product.objects.order_by('-list_date')

    if('keywords' in request.GET):
        keywords = request.GET['keywords']
        query_labels = keywords.split()
        queryset_lists=[]
        if(keywords):
            for label in query_labels:
                # queryset_list = queryset_list.filter(title__icontains = keywords)
                queryset_list = queryset_list.filter(Q(brand_name__icontains=label)
                                                     | Q(title__icontains=label)
                                                     | Q(category__name__icontains=label)).distinct()
                queryset_lists.extend(queryset_list)
        # queryset_lists.distinct()
        print(queryset_lists)

    context = {
        'products' : queryset_lists,
        'values' : request.GET
    }

    return render(request, 'listings/search.html',context)


def categories(request):
    categories = Category.objects.all().filter(is_parent=True)

    context = {
        'categories' : categories
    }

    return render(request, 'listings/categories.html',context)


def bestSellers(request):
    return render(request, 'listings/bestSellers.html')

def category(request, category_id):
    categories = Category.objects.all().filter(parent_categ_id = category_id)
    current_cat = Category.objects.all().filter(id = category_id)

    paginator = Paginator(categories, 6)
    page = request.GET.get('page')

    paged_category = paginator.get_page(page)
    current_cat_name = str(current_cat[0])
    context = {
        'categories': paged_category,
        'current_cat': current_cat,
        'current_cat_name':current_cat_name
    }
    print(current_cat_name)
    print(context.get('current_cat'))
    return render(request,'listings/category.html',context)



def offers(request):
    offers = Product.objects.all().filter(is_offer = True)

    paginator = Paginator(offers, 3)
    page = request.GET.get('page')

    paged_offers = paginator.get_page(page)

    context = {
        'offers': paged_offers
    }
    return render(request, 'listings/offers.html',context)


def offer(request,offer_id):
    offer = Product.objects.all().filter(id = offer_id,is_offer=True)
    reviews = ProductsReview.objects.all().filter(product=offer_id)
    context = {
        'offer':offer,
        'reviews': reviews,
    }
    return render(request, 'listings/offer.html',context)


def update_item(request):

    #data mining setup
    # client = RecombeeClient('e-market-dev','S1HpoVU0JuxtjU9ewtvSnAUQh4qgKHTjr2DFbQ30LoADU2S27OsleTi1C23TNVEm')

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    current_user = request.user
    product = Product.objects.get(id=productId)
    product.sold = product.sold + 1
    product.save()
    order, created = Order.objects.get_or_create(user=current_user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if (action == 'add'):
        # r = AddPurchase(current_user.id,product.id,cascade_create=True)
        # client.send(r)
        orderItem.quantity = (orderItem.quantity + 1)
        product.quantity = (product.quantity -1)
        if(product.quantity==0):
            product.in_stock = False
        product.save()
    elif (action == 'remove'):
        orderItem.quantity = (orderItem.quantity - 1)
        product.quantity = (product.quantity + 1)
        product.save()

    orderItem.save()

    if (orderItem.quantity <= 0):
        orderItem.delete()

    print(f'Action: {action}, productId: {productId}')
    return JsonResponse('Item was added',safe=False)



def search_image(request):
    if(request.method == 'GET'):
        current_user = request.user
        form = SearchImageForm(request.POST, request.FILES)
        # if (form.is_valid()):
        #     form.save()

        context = {
            'form': form,
            'user':current_user
        }
        return render(request,'listings/searchImage.html',context)

    else:
        form = SearchImageForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()

        # context = {
        #     'form': form,
        #
        # }

        logo_detec = LogoDetection(r'C:\Users\Youssef\Desktop\LAU\Software_Engineering\EMarket_project\e_market\media\searched_images','per.jpg')
        logos = logo_detec.get_logos()
        print(logos)
        print('here')
        context = search_img(request,logos)
        return render(request, 'listings/search.html', context)

def search_img(request,keywords):
    queryset_list = Product.objects.order_by('-list_date')

    # if('keywords' in request.GET):
    # keywords = request.GET['keywords']

    queryset_lists=[]
    if(keywords):
        for label in keywords:
            # queryset_list = queryset_list.filter(title__icontains = keywords)
            queryset_list = queryset_list.filter(Q(brand_name__icontains=label)
                                                 | Q(title__icontains=label)
                                                 | Q(category__name__icontains=label)).distinct()
            queryset_lists.extend(queryset_list)
    # queryset_lists.distinct()
    print(queryset_lists)

    context = {
        'products' : queryset_lists,
    }

    return context

def product_review(request):
    form = SubmitReviewForm(request.POST or None)
    if(form.is_valid()):
        form.save()
    product_id = form.cleaned_data['product']
    ratings = ProductsReview.objects.filter(product=product_id)
    counter = 0
    total_rating = 0
    for rating in ratings:
        counter = counter+1
        total_rating = total_rating+rating.get("rating")

    avg_rating = total_rating/counter

    product = Product.objects.get(id=product_id)
    product.rating = avg_rating
    product.save()

    return render(request,'listings/SuccessReviewSubmission.html')