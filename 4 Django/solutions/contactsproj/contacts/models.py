from django.db import models
from django.contrib.auth.models import User

# - ContactType
#   - Name
# - Contact
#   - First Name (CharField)
#   - Last Name (CharField)
#   - Email (CharField)
#   - Image (ImageField)
#   - Birthday (DateField)
#   - Type (ForeignKey to ContactType)
#   - User (ForeignKey to User)


class ContactType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# a foreign key establishes a many-to-one relationship between two models
# e.g. a contact type can have many contacts related to it
# the related_name controls how the 'one' refers to the 'many'
# e.g. how a contact type refers to the set of contacts associated with it
# if you don't specify the related_name Django will take the model name, make it lowercase, and add an '_set'

# >>> from contacts.models import Contact, ContactType
# >>> from django.contrib.auth.models import User

# >>> contact_type = ContactType.objects.get(name='Friend')
# >>> contact_type.contacts.all()
# <QuerySet [<Contact: Wendy Carson>, <Contact: Alyssa Lyons>]>

# >>> contact = Contact.objects.get(id=1)  
# >>> contact
# <Contact: Wendy Carson>
# >>> contact.type.name
# 'Friend'

# >>> user = User.objects.get(username='admin')
# >>> user.contacts.all()
# <QuerySet [<Contact: Wendy Carson>, <Contact: Alyssa Lyons>, <Contact: Brian Barber>]>

# https://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django#:~:text=6%20Answers&text=The%20related_name%20attribute%20specifies%20the,suffix%20_set%20%2C%20for%20instance%20User.&text=The%20Django%20documentation%20has%20more%20details.
# https://docs.djangoproject.com/en/3.1/intro/tutorial03/#use-the-template-system


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    birthday = models.DateField()
    type = models.ForeignKey(ContactType, on_delete=models.PROTECT, related_name='contacts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_image(self):
        if self.image:
            return self.image.url
        return '/static/contacts/default_contact_image.png'

    def __str__(self):
        return self.full_name()




# class Blog(models.Model):
#     header_image = models.ImageField(upload_to='blog_images/')