from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    # the text of the poll
    question_text = models.CharField(max_length=200)
    # date the poll was published
    pub_date = models.DateTimeField('date published')
    # the maximum number of votes before we close the poll
    max_votes = models.IntegerField('Maximum votes')
    # whether the poll is closed
    closed = models.BooleanField()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def count_votes(self):
        output = 0
        # iterate over the choices for this question
        for choice in self.choices.all():
            # add up the votes
            output += choice.votes
        # return the total
        return output

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
    def percentage_votes(self):
        total_votes = self.question.max_votes
        return round(self.votes/total_votes*100, 2)


