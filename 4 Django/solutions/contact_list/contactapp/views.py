from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import City, Contact


# Create your views here.

def index(request):
    contacts = Contact.objects.filter(archived=False).order_by('last_name')
    archived_contacts = Contact.objects.filter(archived=True).order_by('last_name')
    context = {
        'contacts': contacts,
        'archived_contacts': archived_contacts
    }
    
    return render(request, 'contactapp/index.html', context)

def detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {
        'contact': contact,
    }
    return render(request, 'contactapp/detail.html', context)
    # return HttpResponse("You're looking at contact wtih id " + str(contact_id))

def create(request):
    cities = City.objects.all()
    context = {
        'cities': cities
    }
    return render(request,'contactapp/create.html', context)

def save_contact(request):

    if request.method == 'GET':
        return HttpResponseRedirect(reverse('contactapp:index'))

    print(request.POST)
    # extract form data into local variables
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    notes = request.POST['notes']
    city_id = request.POST['city_id']
    if city_id != '':
        existing_city = City.objects.get(id=city_id)
    else:
        existing_city = City.objects.get(name='Portland')
    contact = Contact(first_name = first_name, middle_name=middle_name, last_name=last_name, email =email, phone_number = phone_number, notes = notes, city = existing_city  )

    # contact = Contact(first_name = first_name, middle_name=middle_name, last_name=last_name, email =email, phone_number = phone_number, notes = notes, city_id=city_id)

    # create instance of model using data
    contact.save()
    #save the model to the database 
    
    #redirect back to index page
    return HttpResponseRedirect(reverse('contactapp:index'))
    # return render(request, 'contactapp/index.html')
    # return HttpResponse(dict(test))



def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()

    return HttpResponseRedirect(reverse('contactapp:index'))

def delete_contact_form(request):
    contact_id = request.POST['contact_id']
    contact = Contact.objects.get(id=contact_id)
    contact.delete()

    return HttpResponseRedirect(reverse('contactapp:index'))



def archive_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.archived = True
    contact.save()

    return HttpResponseRedirect(reverse('contactapp:index'))
