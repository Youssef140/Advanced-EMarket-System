from django.shortcuts import render
from .models import *
from listings.models import *
from django.http import JsonResponse
import json
# Create your views here.
from listings.models import Product
from orders.models import OrderOffer
import datetime
from django.contrib.auth.models import User
from .utils import cookieCart, cartData,guestOrder
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *


def cart(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    offers = data['offers']
    print(items)

    context = {
        'items':items,
        'order':order,
        'offers':offers,
    }
    return render(request, 'orders/cart.html',context)

def checkout(request):

    data = cartData(request)
    order = data['order']
    items = data['items']
    print(items)

    context ={
        'items':items,
        'order':order,
    }
    return render(request, 'orders/checkout.html',context)


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
    elif(action=='remove'):
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if(orderItem.quantity<=0):
        orderItem.delete()

    print(f'Action: {action}, productId: {productId}')
    return JsonResponse('Item was added',safe=False)

def update_offer(request):
    data = json.loads(request.body)
    offerId = data['offerId']
    action = data['action']

    current_user = request.user
    offer = Product.objects.get(id=offerId)
    order, created = Order.objects.get_or_create(user=current_user, complete=False)
    orderOffer, created = OrderOffer.objects.get_or_create(order=order, offer=offer)

    if(action == 'add'):
        orderOffer.quantity = (orderOffer.quantity+1)
    elif(action=='remove'):
        orderOffer.quantity = (orderOffer.quantity - 1)

    orderOffer.save()

    if(orderOffer.quantity<=0):
        orderOffer.delete()

    print(f'Action: {action}, productId: {offerId}')
    return JsonResponse('Item was added',safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if(request.user.is_authenticated):
        current_user = request.user
        order, created = Order.objects.get_or_create(user=current_user, complete=False)


    else:
        #function getOrder in utils.py
        current_user, order = guestOrder(request,data)


    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    ShippingAddress.objects.create(
        user=current_user,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
    )

    if (total == float(order.get_cart_total)):
        order.complete = True
    order.save()

    return JsonResponse('Payment complete!',safe=False)