from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from participant.models import Participant, ParticipantForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('participant:register'))
    else:
        form = ParticipantForm()
    return render(request, 'participant/register.html', {'form': form})