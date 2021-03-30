from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts),
    path('new/', views.new_post),
    # localhost:8000/edit/5/, localhost:8000/edit/567/
    path('edit/<int:post_id>/', views.edit_post)
]