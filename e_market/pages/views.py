from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Category,Product
from orders.models import Order, OrderItem
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import operator

def index(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    client = RecombeeClient('e-market-dev', 'S1HpoVU0JuxtjU9ewtvSnAUQh4qgKHTjr2DFbQ30LoADU2S27OsleTi1C23TNVEm')
    current_user = request.user

    prods = Product.objects.order_by('-sold')[:5]
    best_sellers = sorted(prods, key=operator.attrgetter('sold'), reverse=True)
    print(f"best_sellers: {best_sellers}")

    # recomender
    if (request.user.is_authenticated):
        print("auth")
        recommended = client.send(RecommendItemsToUser(current_user.id, 5))
        print(request.user.id)
        print(recommended)
    context = {
        'categories' : categories
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')
