from django.core.management import BaseCommand
from vuetodoapp.models import ToDoItem
import lorem

# we can use a sentence for the title
# and a paragraph for the text


class Command(BaseCommand):

    def handle(self, *args, **options):

        for i in range(75):
            s = lorem.sentence()
            p = lorem.paragraph()
            t = lorem.text()
            title = s
            task = p

            todoitem = ToDoItem(title=title, task=task)
            todoitem.save()

    # title = models.CharField(max_length=200)
    # task = models.CharField(max_length=200)
