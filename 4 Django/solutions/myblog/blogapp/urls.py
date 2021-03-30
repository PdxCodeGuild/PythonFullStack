from django.urls import path
from . import views

app_name="blogapp"
urlpatterns = [
    path('', views.index, name='index'),
    # 'create_post/' - the path part of the url in the address bar
    # views.create_post - find the function 'create_post' in views.py
    path('create_post/', views.create_post, name='create_post'),
]

