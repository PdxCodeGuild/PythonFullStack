from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BlogPost

def index(request):
    posts = BlogPost.objects.order_by('-created_date')
    return render(request, 'blog/index.html', {'posts': posts})

def index_vue(request):
    return render(request, 'blog/index_vue.html')

def toggle_favorite(request):
    post_id = request.GET['post_id']
    post = BlogPost.objects.get(id=post_id)
    user = request.user
    # check if the user has favorited this post (is in the set of user that are related to it)
    # either of these if-statements will work
    # if user in post.favorited_by.all():
    response = ''
    if post.favorited_by.filter(id=user.id).exists():
        # if it is, remove it
        post.favorited_by.remove(user)
        response = 'unfavorited'
    else:
        # if it isn't, add it
        post.favorited_by.add(user)
        response = 'favorited'

    return HttpResponse(response)
    
def get_posts(request):
    posts = BlogPost.objects.order_by('-created_date')
    post_data = []
    for post in posts:
        post_data.append({
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'author': post.author.username,
            'favorited': request.user in post.favorited_by.all(),
            'created_date': post.created_date.strftime('%b %d %Y')
        })
    return JsonResponse({'posts': post_data})



