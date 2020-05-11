from django.shortcuts import render
from cowsay.forms import TextForm

# Create your views here.


def index(request):
    form = TextForm()
    return render(request, 'index.html', {'form': form})
