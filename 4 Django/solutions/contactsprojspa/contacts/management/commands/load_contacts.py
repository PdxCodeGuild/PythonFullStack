

from django.core.management.base import BaseCommand

from contacts.models import Contact
import requests
from io import BytesIO
from django.core import files




# # C:\Users\flux\Downloads\profile_images
# # https://randomuser.me/api/portraits/women/21.jpg
# def download_image(url, folder_path):
#     response = requests.get(url)
#     with open()


# https://stackoverflow.com/questions/16174022/download-a-remote-image-and-save-it-to-a-django-model

class Command(BaseCommand):

    def handle(self, *args, **options):
        Contact.objects.all().delete()
        for i in range(50):
            contact_data = requests.get('https://randomuser.me/api/').json()
            contact_data = contact_data['results'][0]
            name = contact_data['name']['first'] + ' ' + contact_data['name']['last']
            age = contact_data['dob']['age']

            contact = Contact(name=name, age=age, image=None)
            contact.save()

            image_url = contact_data['picture']['large']

            image_response = requests.get(image_url)
            image_data = BytesIO()
            image_data.write(image_response.content)
            file_name = image_url.split('/')[-1]
            contact.image.save(file_name, files.File(image_data))
            contact.save()

            print(str(round(i/50*100,2))+'%')






        




        print(name)


        





