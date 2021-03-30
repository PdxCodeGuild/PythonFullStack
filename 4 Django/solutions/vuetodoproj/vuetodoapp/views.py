from django.shortcuts import render, reverse
from .models import ToDoItem
from django.http import HttpResponse, JsonResponse
import json
from django.core.paginator import Paginator
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    return render(request, "vuetodoapp/index.html")


def get_todoitems(request):
    todoitems = ToDoItem.objects.all().order_by("-id").filter(completed=False)
    num_pages = 1
    total = todoitems.count()
    page = request.GET.get("page", 1)
    print(page)
    if "page" in request.GET:
        page = request.GET.get("page", 1)
        paginator = Paginator(todoitems, 5)
        todoitems = paginator.page(page)
        num_pages = paginator.num_pages
        total = paginator.count


    todo_data = []
    for todoitem in todoitems:
        todo_data.append({
            "title": todoitem.title,
            "task": todoitem.task,
            "id": todoitem.id,
        })
    completed_items = ToDoItem.objects.filter(completed=True)
    complete_item_data = []
    for completed_item in completed_items:
        complete_item_data.append({
            "title": completed_item.title,
            "task": completed_item.task,
            "id": completed_item.id,
        })
# 
    num_pages = 1
    completed_total = completed_items.count()
    page = request.GET.get("page", 1)
    print(page)
    if "page" in request.GET:
        page = request.GET.get("page", 1)
        paginator = Paginator(completed_items, 5)
        completed_items = paginator.page(page)
        num_pages = paginator.num_pages
        total = paginator.count




# 
    json_data = {
            "num_pages": num_pages,
            "total": total,
            "todoitems": todoitems,
            "completed_items": completed_items,
    }
    # test = serializers.serialize('json', json_data)
    # print(test)
    return JsonResponse({"todoitems":todo_data,'completed_items': complete_item_data, 'num_pages': num_pages, 'total': total })


def savetodo(request):
    todo_data = json.loads(request.body)
    print(todo_data)
    title = todo_data["title"]
    task = todo_data["task"]
    todoitem = ToDoItem(title = title, task = task)
    todoitem.save()

    return HttpResponse("OK Morty")

def complete_todo(request):
    todoitem_id = request.GET["todoitem_id"]
    todoitems = ToDoItem.objects.get(id=todoitem_id)
    todoitems.completed = True
    todoitems.save()
    return HttpResponse('ok')

def delete_item(request):
    todoitem_id = request.GET["todoitem_id"]
    todoitem = ToDoItem.objects.get(id=todoitem_id)
    todoitem.delete()
    return HttpResponse('ok')



# one view to render the template
# one to respond to json

    # title = models.CharField(max_length=200)
    # task = models.CharField(max_length=200)
