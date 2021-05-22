import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from listings.models import Category,Product
from orders.models import Order, OrderItem
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import operator

def index(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    current_user = request.user
    client = RecombeeClient('e-market-dev', 'S1HpoVU0JuxtjU9ewtvSnAUQh4qgKHTjr2DFbQ30LoADU2S27OsleTi1C23TNVEm')
    prods = Product.objects.order_by('-sold')[:6]
    best_sellers = sorted(prods, key=operator.attrgetter('sold'), reverse=True)
    print(f"best_sellers: {best_sellers}")

    context = {
        'categories': categories,
        'best_sellers':best_sellers,
    }

    # recomender
    # if (request.user.is_authenticated):
    # print("auth")
    if(not request.user.is_authenticated):
        current_user_id = 0
    else:
        current_user_id = current_user.id
    recommended = client.send(RecommendItemsToUser(current_user_id,5,cascade_create=True))
    # print(recommended)
    client = RecombeeClient('e-market-dev', 'S1HpoVU0JuxtjU9ewtvSnAUQh4qgKHTjr2DFbQ30LoADU2S27OsleTi1C23TNVEm')
    current_user = request.user
    recommended = client.send(RecommendItemsToUser(current_user_id, 3))
    print(f"Related products: {recommended}")
    suggested = recommended['recomms']
    suggested_products_id = []
    for r in suggested:
        suggested_products_id.append(r['id'])
    suggested_products = []
    for id in suggested_products_id:
        prod = Product.objects.all().filter(id=id)
        suggested_products.append(prod)
    print(f"related: {suggested_products}")
    context['suggested_products'] = suggested_products

    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')

def update_item(request):

    #data mining setup
    # client = RecombeeClient('emarket-system-dev','pMFS9IsZDdIbx15eIGRKlGTQbmKsVJ3Ctv6x6vgZ1OsB4kmkkVgtvaOUQK89CT0L')

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    current_user = request.user
    print(current_user)
    print(current_user.id)
    product = Product.objects.get(id=productId)
    print(product)
    print(product.id)
    order, created = Order.objects.get_or_create(user=current_user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if(action == 'add'):
        orderItem.quantity = (orderItem.quantity+1)
        if (product.quantity <= 0):
            product.in_stock=False
            product.save()
        else:
            product.quantity = product.quantity -1
            product.save()

    elif(action=='remove'):
        orderItem.quantity = (orderItem.quantity - 1)
        product.quantity = product.quantity + 1
        product.save()
    orderItem.save()

    if(orderItem.quantity<=0):
        orderItem.delete()

    print(f'Action: {action}, productId: {productId}')
    return JsonResponse('Item was added',safe=False)