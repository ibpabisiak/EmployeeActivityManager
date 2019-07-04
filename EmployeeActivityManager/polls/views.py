from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    template = loader.get_template('index.html')

    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# long way to get object or throw 404 if object does not exist
# def details(request, question_id):
#
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExists:
#         raise Http404("Question does not exist.")
#     return render(request, 'details.html', {'question' : question})

# short way to get object or throw 404 if object does not exist
def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'details.html', {'question' : question})

def result(request, question_id):
    return HttpResponse("you are loogin at the result of question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.set(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):

        #redisplay the question voting form:

        return render(request, 'details.html', {
            'question' : question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
