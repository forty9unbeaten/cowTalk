from django.shortcuts import render
from cowsay.forms import TextForm

# Create your views here.


def index(request):
    form = TextForm()
    return render(request, 'index.html', {'form': form, 'output': None})


def history_view(request):
    return render(request, 'history.html')
