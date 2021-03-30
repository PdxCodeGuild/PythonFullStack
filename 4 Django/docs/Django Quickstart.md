
# Django Quickstart

## 1) Project Setup

1. Create a project: `django-admin startproject myproject`, if you get 'command not found', try `python -m django startproject myproject`
2. Move into the project folder `cd myproject`
3. Create the database with built-in models `python manage.py migrate`
4. Create a superuser `python manage.py createsuperuser`
5. Set the timezone in your `settings.py` (e.g. `TIME_ZONE = 'America/Los_Angeles'`) [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## 2) App Setup

1. Create an app `python manage.py startapp myapp`
2. Add `'myapp'` to the list of `INSTALLED_APPS` in `myproject/settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'myapp'
]
```

## 3) Creating a View and a Route

1. In `myapp/views.py` create an index view

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world!')
```

2. Create a `myapp/urls.py` where we'll create a route to get to our view

```python
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('index/', views.index, name='index')
]
```

3. In `myproject/urls.py` add a route to our `myapp/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls'))
]
```

4. Run the server `python manage.py runserver` and in your browser's address bar, type `localhost:8000/myapp/index/` and you should see `hello world!`



## 4) Render a Template

1. Inside your app folder `myapp`, create a folder called `templates`. Inside of that, create a folder with the same name as your app `myapp`. Then inside of that, create your template `index.html`.

```
myproject
    myapp
        templates
            myapp
                index.html
        ...
        admin.py
        models.py
        urls.py
        views.py
    myproject
        ...
        settings.py
        urls.py
    manage.py
```

2. Inside your `index.html`, put some text to make sure the template is being served by django.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>{{ message }}</h1>
  </body>
</html>
```

3. Change your `myapp/views.py` to render the template instead of responding with plain text.

```python
from django.shortcuts import render

def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myapp/index.html', context)
```

4. Go to `localhost:8000/myapp/index/` and you should see `Hello World!` in an `h1` element.

## 5) Define Your Models

1. In `myapp/models.py` write your models

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField()
    
    def __str__(self):
        return self.title + ' - ' + self.author
```

2. Run migrations to create the tables from your models
  - `python manage.py makemigrations`
  - `python manage.py migrate`

3. Add your models to your `myapp/admin.py`

```python
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
```

4. Log into your admin panel `localhost:8000/admin`, you should see your models, and can make sure they work by creating some record

## 6) Render Data in the Template

1. Amend your `myapp/views.py` to retrieve data from the database and pass it to the template.

```python
from django.shortcuts import render
from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.order_by('-date_published')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'myapp/index.html', context)
```

2. Use the data to generate HTML inside your template `myapp/templates/myapp/index.html`.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <ul>
      {% for blog_post in blog_posts %}
      <li>{{ blog_post.title }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

3. Go to `localhost:8000/myapp/index` to see the blog posts you entered into the admin panel.


