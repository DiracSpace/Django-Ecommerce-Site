from django.shortcuts import render
from .models import *

# Create your views here.
def Store(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'store/store.html', context)

def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items' : items}
    return render(request, 'store/cart.html', context)

def Checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)