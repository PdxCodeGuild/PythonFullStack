from django.contrib import admin

from .models import Question, Choice



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
admin.site.register(Choice, ChoiceAdmin)
