from django.shortcuts import render, get_object_or_404
from django.http import	HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
	latest_question_list = Question.objects.all()
	return render(request, 'polls/index.html', {
		'latest_question_list': latest_question_list
	})


def detail(request, question_id):	# Detalle de una pregunta
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {
		'question': question
	})


def results(request, question_id):	# Cantidad de votos de una pregunta
	return HttpResponse(f'Estas viendo los resultados de la pregunta numero {question_id}')


def votes(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': 'no elegiste una respuesta'
		})
	
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=[question.id]))