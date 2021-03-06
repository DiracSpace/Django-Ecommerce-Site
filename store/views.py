from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json, datetime

def Store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']
    
    products = Product.objects.all()
    context = {'products' : products, 'cartItems' : cartItems, 'shipping' : False}
    return render(request, 'store/store.html', context)

@login_required(login_url="/accounts/login")
def Dashboard(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.all()
        for order in orders:
            if order.complete == True and order.customer == customer:
                items = list(OrderItem.objects.filter(order=order))
    context = {'items' : items}
    return render(request, 'store/dashboard.html', context)

@login_required(login_url="/accounts/login")
def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']

        for item in cart:
            cartItems += cart[item]['quantity']
    
    context = {'items' : items, 'order' : order, 'cartItems' : cartItems, 'shipping' : False}
    return render(request, 'store/cart.html', context)

@login_required(login_url="/accounts/login")
def Checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']
    
    context = {'items' : items, 'order' : order, 'cartItems' : cartItems, 'shipping' : False}
    return render(request, 'store/checkout.html', context)

@login_required(login_url="/accounts/login")
def updateItem(request):
    data = json.loads(request.body)
    productId = data['pid']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse("Item added", safe=False)

@login_required(login_url="/accounts/login")
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create (
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode']
            )
    else:
        print ('user not logged in')
    return JsonResponse("payment accepted", safe=False)