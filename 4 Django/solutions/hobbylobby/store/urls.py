from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_products),
    path('cart/', views.cart),
    path('faq/', views.faq)
]