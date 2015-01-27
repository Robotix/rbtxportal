from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from participant.models import Participant, ParticipantForm, FindForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant_object = form.save()
            return HttpResponseRedirect(reverse('participant:status', args=(participant_object.id,)))
    else:
        form = ParticipantForm()
    return render(
        request, 
        'participant/register.html', 
        {'form': form})

def find(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            participant_object = get_object_or_404(Participant, mobileNo= request.POST['mobile'])
            return HttpResponseRedirect(reverse('participant:status', args=(participant_object.id,)))
    else:
        form = FindForm()
    return render(
        request,
        'participant/find.html',
        {'form': form})

def search(request):
    if request.method == 'POST':
        try:
            participant_object = get_object_or_404(Participant, mobileNo= request.POST['mobile'])
            return HttpResponseRedirect(reverse('participant:status', args=(participant_object.id,)))
        except:
            return render(
                request,
                'participant/status.html',
                { 'content': 'You have registered more than once. Contact the helpdesk.'})
    else:
        return Http404

def status(request, id):
    participant_object = get_object_or_404(Participant, id=id)
    return render(
        request, 
        'participant/status.html',
        { 'content': 'Your participant ID is %d' %(participant_object.id)})
