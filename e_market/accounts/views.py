from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages


def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pwd']
        password2 = request.POST['pwd2']

        if(password == password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'This username is already in use')
                return redirect('register')
            else:
                if (User.objects.filter(email=email).exists()):
                    messages.info(request, 'This email is already in use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.set_password(password)

                    #Login after register
                    # auth.login(request, user)
                    # messages.success(request,"You are now loged in")
                    # return redirect('index')
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')
        else:
            # messages.error(request,'Passwords does not match')
            return redirect('register')

    #     user = User.objects.create_user(username=username, first_name= first_name, last_name=last_name, email=email, password=password)
    #     auth.login(request,user)
    #
    #     return redirect('/')
    else:
        return render(request,'accounts/register.html')

def login(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)

        user = authenticate(request,username=username,password=password)

        print(user)

        if(user is not None):
            auth_login(request, user)
            # messages.success(request,'You are now logged in')
            print('exists')
            return redirect('index')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')


    else:
        return render(request,'accounts/login.html')



def logout(request):
    if (request.method == 'POST'):
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def editProfile(request):
    current_user = request.user
    user = User.objects.all().get(id=current_user.id)

    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.user_name = user_name
        user.save()

    return render(request,'accounts/editProfile.html')

def editPassword(request):
    return render(request,'accounts/editPassword.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')