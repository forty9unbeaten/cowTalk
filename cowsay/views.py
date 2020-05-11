from django.shortcuts import render
from cowsay.forms import TextForm
from cowsay.models import CowSentence
import subprocess


# Create your views here.


def index(request):
    # POST request handling
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            cowText = form.cleaned_data['text']

            # run cowsay subprocess and capture output
            cowsay = subprocess.run(
                ['cowsay', cowText],
                stdout=subprocess.PIPE)
            output = cowsay.stdout.decode()
            # create new database instance with subprocess output
            new_entry = CowSentence(
                cow_text=output
            )
            new_entry.save()

            return render(request,
                          'index.html',
                          {
                              'form': TextForm(),
                              'output': output
                          })

    # GET request handling
    form = TextForm()
    return render(request,
                  'index.html',
                  {
                      'form': form,
                      'output': None
                  })


def history_view(request):
    all_entries = CowSentence.objects.all()
    number_of_entries = len(all_entries)

    if number_of_entries > 10:
        history = all_entries[number_of_entries - 10:]
    elif number_of_entries > 0:
        history = all_entries
    else:
        history = None

    return render(request,
                  'history.html',
                  {
                      'history': history
                  })
