from django.shortcuts import render
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(max_age=180)
def Store(request):
    context = {}
    return render(request, 'store/store.html', context)

@cache_control(max_age=180)
def Cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

@cache_control(max_age=180)
def Checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)