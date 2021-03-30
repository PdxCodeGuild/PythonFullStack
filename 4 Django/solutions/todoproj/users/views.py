from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_page(request):
    message = request.GET.get('message', '')
    if message == 'user_already_exists':
        message = 'A user with that username already exists'
    return render(request, 'users/register.html', {'message': message})


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    print(username)
    print(email)
    print(password)

    if User.objects.filter(username=username).exists():
        # return render(request, 'users/register.html', {'message': 'User already exists'})
        return HttpResponseRedirect(reverse('users:register_page')+'?message=user_already_exists')


    user = User.objects.create_user(username, email, password)
    
    return HttpResponseRedirect(reverse('todoapp:index'))



def login_page(request):
    return render(request, 'users/login.html', {})


def login_user(request):
    # print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('todoapp:index'))
    else:
        return render(request, 'users/login.html', {'message': 'Username and/or password do not match'})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login_page'))

