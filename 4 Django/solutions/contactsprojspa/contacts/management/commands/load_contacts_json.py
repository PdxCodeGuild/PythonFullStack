

from django.core.management.base import BaseCommand

from contacts.models import Contact
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./contacts/management/commands/contacts.json', 'r') as file:
            contents = file.read()
        data = json.loads(contents)
        for contact in data['contacts']:
            name = contact['name']
            age = contact['age']

            print(name)
            print(age)

            # create your model and save it




        





