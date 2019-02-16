from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from django.contrib.auth.models import User
from .models import Question


# Create your views here.
def index(request):
	latest_question_list = Question.objects.all()
	context = {'latest_question_list': latest_question_list, 'user':None}
	if request.user.is_authenticated:
		context['user'] = request.user
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': 'You didn\'t select a choice.'
			})
	else:
		selected_choice.vote += 1
		selected_choice.save()		
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def signup(request):
	context = {'error':False}
	if request.method == 'GET':
		return render(request, 'polls/signup.html', context)
	if request.method == 'POST':
		print(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = User.objects.create_user(username=username, password=password)
			auth.login(request, user)
			return HttpResponseRedirect(reverse('polls:index'))
		except:
			context['error'] = f"Username '{username}' already exists."
			return render(request, 'polls/signup.html', context)

def login(request):
	context = {'error':False}
	if request.method == 'GET':
		return render(request, 'polls/login.html')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = auth.authenticate(username=username, password=password)
			auth.login(request, user)
			return HttpResponseRedirect(reverse('polls:index'))
		except:
			context['error'] = 'Invalid Login Credentials'
			return render(request, 'polls/login.html', context)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('polls:login'))
