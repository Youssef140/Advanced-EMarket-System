import json
from .models import *
from listings.models import Product
from django.contrib.auth.models import User

def cookieCart(request):

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    # cart = json.loads(request.COOKIES['cart'])
    print('cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cart_items = order['get_cart_items']

    for i in cart:
        try:
            cart_items += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'photo_main': product.photo_main,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
        except:
            pass
    return {'cart_items':cart_items,'order':order,'items':items}


def cartData(request):
    if(request.user.is_authenticated):
        current_user = request.user
        order, created = Order.objects.get_or_create(user=current_user, complete=False)
        #geting all order items that have that current item as parent
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        items = cookieData['items']
        cart_items = cookieData['cart_items']
    return {'cart_items':cart_items,'order':order,'items':items,}

def guestOrder(request,data):
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']
    current_user, created = User.objects.get_or_create(
        email=email,
        username=name,
    )
    current_user.save()

    order = Order.objects.create(
        user=current_user,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return current_user, order