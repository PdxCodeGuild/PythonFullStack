from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .models import Contact
import json



'''
Feature 1: display contacts in page
- view which renders a template containing a "hello world" vue app
- write model, run migrations, add to admin panel, enter dummy data
- view which gets data from the database and responds with json
- modified our template to do an axios call to get the json data
- assigned the data from the api to our app data and displayed it in the html

Feature 2: save a contact
- modify our template to have input fields and a button
- connected the input fields and button to our vue app
- in the button event, send an ajax post to a view
- create a view to receive the ajax post (print(request.body))
- created a record from the ajax post data and saved it to the database
- refreshed the data in the template after saving the contact
'''

def index(request):
    return render(request, 'contacts/index.html', {})

def get_contacts(request):
    # return JsonResponse({'a': 1, 'b': 2})
    
    # get all the contacts out of the database
    contacts = Contact.objects.filter(archived=False).order_by('-id')
    num_pages = 1
    total_records = contacts.count()

    if 'search' in request.GET:
        search = request.GET['search']
        contacts = contacts.filter(name__icontains=search)

    # pagination
    if 'page' in request.GET:
        page = request.GET['page']
        paginator = Paginator(contacts, 5)
        contacts = paginator.page(page)
        num_pages = paginator.num_pages
        total_records = paginator.count


    # turning our queryset of contacts into a list of dictionaries
    # json can only contain: null, boolean, string, number, lists, objects
    contact_data = []
    for contact in contacts:
        contact_data.append({
            'id': contact.id,
            'name': contact.name,
            'age': contact.age,
            'image': contact.image.url if contact.image else '',
        })
    # print(contact_data)
    json_data = {
        'contacts': contact_data,
        'num_pages': num_pages,
        'total_records': total_records
    }
    return JsonResponse(json_data)

def create_contact(request):
    # print(request.body)
    contact_data = json.loads(request.body)
    name = contact_data['name']
    age = contact_data['age']

    contact = Contact(name=name, age=age, image=None)
    contact.save()

    # return JsonResponse({
    #         'id': contact.id,
    #         'name': contact.name,
    #         'age': contact.age,
    #         'image': contact.image.url if contact.image else '',
    #     })

    return HttpResponse('ok')

def create_contact2(request):
    # print(request.POST)
    # print(request.FILES)

    contact = Contact(
        name = request.POST['name'],
        age = request.POST['age'],
        image = request.FILES['contact_image']
    )
    contact.save()

    return HttpResponse('ok')



def archive_contact(request):
    # print(request.GET)
    contact_id = request.GET['contact_id']
    contact = Contact.objects.get(id=contact_id)
    contact.archived = True
    contact.save()
    return HttpResponse('ok')


def archive_contact2(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.archived = True
    contact.save()
    return HttpResponse('ok')

def archive_contact3(request):
    contact_data = json.loads(request.body)
    contact_id = contact_data['contact_id']
    contact = Contact.objects.get(id=contact_id)
    contact.archived = True
    contact.save()
    return HttpResponse('ok')



def delete_contact(request):
    contact_id = request.GET['contact_id']
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return HttpResponse('ok')


def delete_archived_contacts(request):
    contacts = Contact.objects.filter(archived=True)
    contacts.delete()
    return HttpResponse('ok')