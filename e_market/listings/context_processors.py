from .models import Category
from orders.models import Order, OrderItem

categories = Category.objects.all()

def get_categories(request):
    return {
        'categories': categories
    }


def get_order_items(request):
    if (request.user.is_authenticated):
        current_user = request.user
        order, created = Order.objects.get_or_create(user=current_user, complete=False)
        # geting all order items that have that current item as parent
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    return {
        'cart_items': cart_items
    }