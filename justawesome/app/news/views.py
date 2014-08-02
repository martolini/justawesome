from django.shortcuts import render

def nominate_view(request):
	return render(request, 'nominate.jade')

