from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import JsonResponse
from .forms import SignupForm

def usersignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.POST.get('next')) if 'next' in request.POST else redirect('coronas:store')
    else:
        form = UserCreationForm()
    context = {"form" : form}
    return render(request, 'accounts/signup.html', context)

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('coronas:store')
    else:
        form = AuthenticationForm()
    context = {'form' : form}
    return render(request, 'accounts/login.html', context)

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('coronas:store')

'''
def usersignup(request):
    return JsonResponse("user signup", safe=False)
'''