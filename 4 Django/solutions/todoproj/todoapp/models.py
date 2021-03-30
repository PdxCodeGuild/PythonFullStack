from django.db import models
from django.contrib.auth.models import User



class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' (' + str(self.todo_items.count()) + ')'


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todo_items')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='todo_items')
    created_date = models.DateTimeField()

    def __str__(self):
        return self.text + ' (' + self.priority.name + ') ' + self.user.username


