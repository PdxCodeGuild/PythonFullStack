from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ', ' + self.state
    

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='contacts')
    notes = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField()
    
    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
    