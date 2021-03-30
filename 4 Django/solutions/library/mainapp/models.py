from django.db import models



class Book(models.Model):
    key = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=100)
    year_published = models.IntegerField()

    def __str__(self):
        return self.title

