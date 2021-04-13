from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST.get('pwd')
        password2 = request.POST.get('pwd2')

        user = User.objects.create_user(username=username, first_name= first_name, last_name=last_name, email=email, password=password)
        auth.login(request,user)

        return redirect('/')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwdd']

        print(username)
        print(password)

        user = auth.authenticate(username=username,password=password)

        print(user)

        if user is not None:
            auth.login(request,user)
            print('exists')
            return redirect('index')
        else:
            print('not exists')
            return redirect('login')


    else:
        return render(request,'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')