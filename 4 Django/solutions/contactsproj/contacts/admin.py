from django.contrib import admin


from .models import Contact, ContactType

admin.site.register(Contact)
admin.site.register(ContactType)


