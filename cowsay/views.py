from django.shortcuts import render
from cowsay.forms import TextForm
from cowsay.models import CowSentence
from cowsay.utils import run_cowsay, make_entry_dict


# Create your views here.


def index(request):
    # POST request handling
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            cowText = form.cleaned_data['text']
            # create a new database instance storing text string
            new_db_entry = CowSentence(
                cow_text=cowText
            )
            new_db_entry.save()

            # run cowsay subprocess function and capture output
            output = run_cowsay(cowText)

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
        history = [make_entry_dict(entry)
                   for entry in all_entries[number_of_entries - 10:]]

    elif number_of_entries > 0:
        history = [make_entry_dict(entry)
                   for entry in all_entries]

    else:
        history = None

    return render(request,
                  'history.html',
                  {
                      'history': history
                  })
