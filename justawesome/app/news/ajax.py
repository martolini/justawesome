from django_ajax.decorators import ajax

@ajax
def nominate_ajax(request):
	print request.POST