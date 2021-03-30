from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('receive_form/', views.receive_form),
    path('about/', views.about),
    path('contact/', views.contactus),
]

