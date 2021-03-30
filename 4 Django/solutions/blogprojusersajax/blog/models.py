from django.db import models
from users.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='authored_posts')
    favorited_by = models.ManyToManyField(User, related_name='favorited_posts', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' by ' + self.author.username + ' on ' + self.created_date.strftime('%b %d %Y')


