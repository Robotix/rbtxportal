from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from team.models import Team

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('team:register'))
    else:
        form = TeamForm()
    return render(request, 'team/register.html', {'form': form})