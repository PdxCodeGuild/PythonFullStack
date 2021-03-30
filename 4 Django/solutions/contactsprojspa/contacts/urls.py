

from django.urls import path

from . import views


app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('create_contact2/', views.create_contact2, name='create_contact2'),
    path('archive_contact/', views.archive_contact, name='archive_contact'),
    path('archive_contact2/<int:contact_id>/', views.archive_contact2, name='archive_contact2'),
    path('archive_contact3/', views.archive_contact3, name='archive_contact3'),
    path('delete_contact/', views.delete_contact, name='delete_contact'),
    path('delete_archived_contacts/', views.delete_archived_contacts, name='delete_archived_contacts'),
]




