from django.urls import path
from . import views

app_name = "vuetodoapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("get_todoitems", views.get_todoitems, name="get_todoitems"),
    path("savetodo/", views.savetodo, name="savetodo"),
    path("complete_todo/", views.complete_todo, name="complete_todo"),
    path("delete_item/", views.delete_item, name="delete_item"),
]


