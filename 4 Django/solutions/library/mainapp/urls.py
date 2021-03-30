
from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('search_books/', views.search_books, name='search_books'),
    path('favorite_book/', views.favorite_book, name='favorite_book'),
    path('favorites/', views.favorites, name='favorites')
]
