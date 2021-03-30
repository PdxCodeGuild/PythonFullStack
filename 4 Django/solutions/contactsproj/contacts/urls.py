
from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('detail/<int:contact_id>/', views.detail, name='detail'),
    path('edit/<int:contact_id>/', views.edit, name='edit'),
]