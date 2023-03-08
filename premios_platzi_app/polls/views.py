from django.shortcuts import render, get_object_or_404
from django.http import	HttpResponse
from .models import Question 

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
	return HttpResponse(f'Estas votando a la pregunta numero {question_id}')