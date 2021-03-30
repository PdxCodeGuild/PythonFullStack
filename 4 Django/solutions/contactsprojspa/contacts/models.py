from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    image = models.ImageField(upload_to='contact_images/', null=True, blank=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name



