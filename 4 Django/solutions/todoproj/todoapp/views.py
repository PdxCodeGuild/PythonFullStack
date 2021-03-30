from django.shortcuts import render, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem, Priority

@login_required
def index(request):
    # if request.user.is_authenticated:
    #     print(request.user.username)
    #     print(request.user.email)
    #     print(request.user.date_joined)

    todo_items = request.user.todo_items.all()
    priorities = Priority.objects.all()
    
    # if request.user.is_authenticated:
    #     todo_items = request.user.todo_items.all()
    # else:
    #     return HttpResponseRedirect(reverse('users:login_page'))
    
    # todo_items = TodoItem.objects.all()
    # print(todo_items)
    # for todo_item in todo_items:
    #     print(todo_item.notes)
    
    context = {
        'todo_items': todo_items,
        'priorities': priorities
    }
    return render(request, 'todoapp/index.html', context)

@login_required
def add_todo(request):
    # print(request.POST)

    todo_text = request.POST['todo_text']
    todo_priority_id = request.POST['todo_priority_id']

    priority = Priority.objects.get(id=todo_priority_id)

    todo_item = TodoItem(text=todo_text, priority=priority, user=request.user, created_date=timezone.now())
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))