import json
import os,io
from google.cloud import vision, vision_v1
from google.cloud.vision_v1 import types
import pandas as pd
from .models import Category
from orders.models import Order, OrderItem
from orders.utils import cartData, cookieCart

categories = Category.objects.all()

def get_categories(request):
    return {
        'categories': categories
    }


def get_order_items(request):
    data = cartData(request)
    cart_items = data['cart_items']
    # if (request.user.is_authenticated):
    #     current_user = request.user
    #     order, created = Order.objects.get_or_create(user=current_user, complete=False)
    #     # geting all order items that have that current item as parent
    #     items = order.orderitem_set.all()
    #     cart_items = order.get_cart_items
    # else:
    #     # cookieData = cookieCart(request)
    #     # cart_items = cookieData['cart_items']
    #     try:
    #         cart = json.loads(request.COOKIES['cart'])
    #     except:
    #         cart={}
    #     items = []
    #     order = {'get_cart_total': 0, 'get_cart_items': 0}
    #     cart_items = order['get_cart_items']
    #
    #     for i in cart:
    #         cart_items += cart[i]["quantity"]
    #

    return {
        'cart_items': cart_items
    }


