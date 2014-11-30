from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'index.html')

def status(request, event, id):
	try:
		team = teams.objects.get(event= event, id= id)
	except:
		raise Http404

	return render(request, 'status.html', {'event': event, 'id': id, 'status':team.status})

def submit(request):
	raise Http404