from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserCreateForm, UserLoginForm
from store.models import Customer

def usersignup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.get_or_create(user_id=user.id, name=user.username, email=user.email)
            return redirect('accounts:login')
    else:
        form = UserCreateForm()
    context = {"form" : form}
    return render(request, 'accounts/signup.html', context)

def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('coronas:store')
    else:
        form = UserLoginForm()
    context = {'form' : form}
    return render(request, 'accounts/login.html', context)

def userlogout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('coronas:store')