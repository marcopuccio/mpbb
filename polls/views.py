
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render

from polls.forms import CreateQuestionForm
from polls.models import  Choice, Question


def index(request):
    """
    App index view.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    Question detail View
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    Question results
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """
    Question vote action.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        question.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def most_voted(request):
    """
    Returns the five most voted questions DESC ordered.
    """

    most_voted_question_list = Question.objects.all().order_by('-total_votes')[:5]
    context = {'most_voted_question_list': most_voted_question_list}
    return render(request, 'polls/most_voted.html', context)

def create_question(request):
    """
    Create Question
    """
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Get Question Text (Required)
            question_text = data.get('question_text')

            # Create a empty list to group the choice text
            choices = []
            for k, v in data.iteritems():
                if k != 'question_text' and v != '':
                    choices.append(v)

            # Instance and save a Question 
            question = Question(question_text=question_text)
            question.save()

            # Create choices for question
            for choice_text in choices:
                question.choice_set.create(choice_text=choice_text)

            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = CreateQuestionForm()

    context = {'form': form}
    return render(request, 'polls/create.html', context)
