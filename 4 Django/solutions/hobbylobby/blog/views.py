from django.shortcuts import render
from django.http import HttpResponse

def list_posts(request):
    return HttpResponse('list of blog posts')

def new_post(request):
    return HttpResponse('new blog post')

def edit_post(request, post_id):
    return HttpResponse('edit blog post with id ' + str(post_id))

