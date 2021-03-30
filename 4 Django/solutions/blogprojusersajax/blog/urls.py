

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('index_vue/', views.index_vue, name='index_vue'),
    path('toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('get_posts/', views.get_posts, name='get_posts')
]

