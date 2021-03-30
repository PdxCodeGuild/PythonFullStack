from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    # localhost:8000/post/5/
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/save/', views.save_post, name='save_post'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/edit/save/', views.save_edited_post, name='save_edited_post'),
]
