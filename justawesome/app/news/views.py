from django.shortcuts import render
from .models import Article

def nominate_view(request):
	return render(request, 'nominate.jade')

def vote_view(request):
	return render(request, 'vote.jade', {'step_nr': 1, 'articles': Article.objects.all()[:3]})

def home_view(request):
	return render(request, 'home.jade', {'articles': Article.objects.all()[:3], 'can_see': False})

def article_view(request):
	return render(request, 'article.jade', {'articles': Article.objects.all()})

def about_view(request):
	return render(request, 'about.jade')


