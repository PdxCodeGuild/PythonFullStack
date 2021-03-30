from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Contact, ContactType

@login_required
def home(request):
    contacts = request.user.contacts.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/home.html', context)

@login_required
def create(request):
    if request.method == 'POST':

        # print('*'*100)
        # print(request.POST)
        # print(request.FILES)
        # print(request.FILES['image'])
        # print(type(request.FILES['image']))
        # print('*'*100)

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        image = request.FILES.get('image', None)
        birthday = request.POST['birthday']
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        type_id = request.POST['type_id']
        contact_type = ContactType.objects.get(id=type_id)
        user = request.user
        
        contact = Contact(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            image=image,
                            birthday=birthday,
                            type=contact_type,
                            user=user)
        contact.save()

        return HttpResponseRedirect(reverse('contacts:home'))


    types = ContactType.objects.order_by('name')
    context = {
        'types': types
    }
    return render(request, 'contacts/create.html', context)


@login_required
def detail(request, contact_id):

    # contact = request.user.contacts.filter(id=contact_id).first()
    # if contact is None:
    #     raise Http404
    
    # contact = Contact.objects.filter(user=request.user, id=contact_id).first()
    # if contact is None:
    #     raise Http404

    contact = get_object_or_404(Contact, id=contact_id)
    # is the user for this contact the same as the logged in user
    if contact.user.id != request.user.id:
        raise Http404
    return render(request, 'contacts/detail.html', {'contact': contact})


@login_required
def edit(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id)
    # is the user for this contact the same as the logged in user
    if contact.user.id != request.user.id:
        raise Http404

    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        birthday = request.POST['birthday']
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        type_id = request.POST['type_id']
        contact_type = ContactType.objects.get(id=type_id)
        user = request.user

        contact.first_name = first_name
        contact.last_name = last_name
        contact.email = email
        contact.birthday = birthday
        contact.type = contact_type
        contact.user = user

        if 'clear_image' in request.POST:
            contact.image = None
        elif 'image' in request.FILES:
            image = request.FILES['image']
            contact.image = image

        contact.save()

        return HttpResponseRedirect(reverse('contacts:home'))

    types = ContactType.objects.order_by('name')
    context = {
        'contact': contact,
        'types': types
    }
    return render(request, 'contacts/edit.html', context)