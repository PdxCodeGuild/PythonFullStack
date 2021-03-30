from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def index(request):
    open_questions = Question.objects.filter(closed=False).order_by('-pub_date')
    all_questions = Question.objects.order_by('pub_date')
    context = {
        'open_questions': open_questions,
        'all_questions': all_questions
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    if question.closed:
        return HttpResponseRedirect(reverse('polls:index'))
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    print(request.POST)
    
    question = get_object_or_404(Question, pk=question_id)

    if 'choice' in request.POST:
        choice_id = request.POST['choice']
        selected_choice = Choice.objects.filter(id=choice_id).first()
        if selected_choice is not None:
            selected_choice.votes += 1
            selected_choice.save()

            if question.count_votes() == question.max_votes:
                question.closed = True
                question.save()

            return HttpResponseRedirect(reverse('polls:results', args=[question.id]))
    return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
    })
    

        