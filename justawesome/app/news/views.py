from django.shortcuts import render
from .models import Article

def nominate_view(request):
	return render(request, 'nominate.jade')

def vote_view(request):
	return render(request, 'vote.jade', {'step_nr': 2, 'articles': Article.objects.all()[:3]})

def home_view(request):
	return render(request, 'home.jade')


