from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import BlogPost

# Create your views here.
def index(request):

    print(request.method)
    print(request.POST)

    # search_text = request.POST.get('search_text', '')
    # if request.method == 'POST':
    if 'search_text' in request.POST:
        search_text = request.POST['search_text']
        posts = BlogPost.objects.filter(title__icontains=search_text)
    else:
        search_text = ''
        posts = BlogPost.objects.all()


    # search_text = request.POST['search_text']
    # print(search_text)
    #grabs all info pertaining to blog posts.
    # posts = BlogPost.objects.all()
    # for post in posts:
    #     print(post.title)
    #     print(post.body)
    # titles = BlogPost.objects.all()
    # print(posts)

    context = {
        'posts':posts,
        'search_text': search_text
    }
    return render(request, "blogapp/index.html", context)


def create_post(request):
    # print(request.POST)
    # return HttpResponse('ok')

    # 1) get form data out of request.POST
    blog_title = request.POST['blog_post_title']
    blog_body = request.POST['blog_post_body']

    # 2) take the title and body, instantiate our model
    blog_post = BlogPost(title=blog_title, body=blog_body, created_date=timezone.now())
    # blog_post = BlogPost(title='My First Post', body='When I was five....')

    # 3) save it to the database
    blog_post.save()

    # 4) redirect back to the index page
    # print(reverse('blogapp:index')) # ''
    # print(reverse('blogapp:create_post')) # /create_post/
    return HttpResponseRedirect(reverse('blogapp:index'))

