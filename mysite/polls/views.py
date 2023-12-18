from django.shortcuts import render
from .models import polls
from .forms import pollsForm

def index(request):
	if request.method == 'POST':
		form = pollsForm(request.POST)

		if form.is_valid():
			form.save()
		else:
			print("hello")
	else:
		form = pollsForm

	dados_polls = polls.objects.all

	return render(request, "index.html", {"dados_polls":dados_polls,"form":form})

def blog(request):
	return render(request, "blog.html") 

