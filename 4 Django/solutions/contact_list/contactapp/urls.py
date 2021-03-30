from django.urls import path
from . import views

app_name = 'contactapp'
urlpatterns = [
    path('', views.index, name='index'),
    # localhost:8000/contactapp/detail/5/
    path('create/', views.create, name='create'),
    path('savecontact/', views.save_contact, name='savecontact'),
    path('detail/<int:contact_id>/', views.detail, name='detail'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('archive/<int:contact_id>/', views.archive_contact, name='archive_contact'),
    path('delete_contact_form/', views.delete_contact_form, name='delete_contact_form')
]