
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register_page, name='register_page'),
    path('register_user/', views.register_user, name='register_user'),
    path('login/', views.login_page, name='login_page'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user')
]






