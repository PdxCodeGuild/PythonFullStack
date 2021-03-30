from django.db import models
from django.utils import timezone

# Create your models here.


# class Model:
#     def __init__(self, **kwargs):
#         ...

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    # deleted_date = models.DateTimeField(null=True)

    '''
    three places __str__ is used by django

    1) admin panel

    2) if you print an instance of the model
    blog_post = BlogPost.objects.get(id=1)
    print(blog_post)

    3) if you render an instance into the template
    {{blog_post}}
    '''
    def __str__(self):
        return self.title + ': ' + self.body[:20] + '...'











# class BlogPost:
#     static_prop = 5

#     def __init__(self, title, body):
#         self.title = title
#         self.body = body
    
#     def __str__(self):
#         return self.title

# blog_post = BlogPost('My Blog Post', 'Lorem ipsum delorum est...')
# print(blog_post.title) # My Blog Post
# print(blog_post.body) # Lorem ipsum

# print(BlogPost.static_prop)





