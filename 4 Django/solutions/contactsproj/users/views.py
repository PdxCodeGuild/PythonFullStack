from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import django.contrib.auth




# def register_page(request):
#     ...

#     message = request.GET['message']
#     return render(request, 'users/register.html', {})


# def register_user(request):
#     ...

#     username = request.POST['username']
#     if User.objects.filter(username=username).exists():
#         return HttpResponseRedirect(reverse('users:register')+'?message=bad_username')






def register(request):

    # check if we're receiving a form submission
    if request.method == 'POST':
        
        # get the data out of the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # check if the user already exists in the database
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'message': 'A user with that username already exists'})

        if len(password) < 10:
            return render(request, 'users/register.html', {'message': 'The password must be 10 characters or longer'})

        # create the user
        user = User.objects.create_user(username, email, password)
        # log the user in
        django.contrib.auth.login(request, user)
        # redirect to the home page
        return HttpResponseRedirect(reverse('contacts:home'))

    return render(request, 'users/register.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'users/login.html', {'message': 'No user found with that username and password'})
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('contacts:home'))
    return render(request, 'users/login.html', {})


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))