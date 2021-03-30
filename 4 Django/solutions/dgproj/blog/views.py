from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})



# render the template for creating a new post
@login_required
def post_new(request):
    return render(request, 'blog/post_new.html', {})

# receive the form submission from the template rendered by 'post_new'
def save_post(request):
    print(request.POST)

    # getting the fields out of the form data (look at the name attribute of the input elements)
    title = request.POST['title']
    text = request.POST['text']

    # creating an instance of our model, listing out all the fields and their values
    post = Post(title=title, text=text, author=request.user, published_date=timezone.now())
    # saving the instance of the model to the database (adding a row to the table)
    post.save()

    # redirecting back to the index page (part 3 of the official django tutorial)
    # the same as {% url 'blog:post_detail' post.id %} in the template
    return HttpResponseRedirect(reverse('blog:post_detail', args=(post.id,)))


# render a template for editing an existing blog post
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_edit.html', {'post': post})

# receiving the form submission from the template rendered by 'post_edit'
def save_edited_post(request, post_id):
    print(request.POST)
    
    # looking yp the post with the given id
    post = get_object_or_404(Post, id=post_id)

    # getting the values out of the form data
    # and assigning them to properties on our model
    post.title = request.POST['title']
    post.text = request.POST['text']
    # saving the post to our database
    post.save()

    # redirecting to the post detail page
    return HttpResponseRedirect(reverse('blog:post_detail', args=(post.id,)))



# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog:post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})