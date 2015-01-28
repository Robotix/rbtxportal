from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from team.models import Team, TeamForm, FindForm
from participant.models import Participant

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team_object = Team(
            	number = len(Team.objects.filter(event= form.cleaned_data['event']))+1,
            	participant_number = form.cleaned_data['number_of_participants'],
                event = form.cleaned_data['event'],
                street = form.cleaned_data['street'],
                locality = form.cleaned_data['locality'],
                city = form.cleaned_data['city'],
                state = form.cleaned_data['state'],
                pin = form.cleaned_data['pin'],
            	)
            team_object.save()
            for i in range(int(team_object.participant_number)):
                team_object.participant.add(get_object_or_404(Participant, id = form.cleaned_data['participant_no_%d' %(i+1)]))
            return HttpResponseRedirect(reverse('team:status', args=(team_object.id,)))
    else:
        form = TeamForm()
    return render(request, 'team/register.html', {'form': form})

def status(request, id):
    team_object = get_object_or_404(Team, id = id)
    return render(
        request,
        'team/status.html',
        { 'content': 'You are a part of ' + str(team_object)})

def find(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            team_object = get_object_or_404(Team, event = form.cleaned_data['event'], participant = get_object_or_404(Participant, id = form.cleaned_data['participant_id']))
            print team_object
            return HttpResponseRedirect(reverse('team:status', args=(team_object.id,)))
    else:
        form = FindForm()
    return render(
        request,
        'team/find.html',
        {'form': form})

def search(request):
    if request.method == 'POST':
        participant_object = get_object_or_404(Participant, id= request.POST['participant_id'])

        return HttpResponseRedirect(reverse('team:status', args=(participant_object.id,)))
    else:
        return Http404