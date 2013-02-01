from datetime import datetime
from string import upper
import urllib2

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render_to_response

from eventmanager.forms import *
from eventmanager.models import *
from eventmanager.view_utils import *

def _construct_err(txt):
    return render_to_response('error.html', { 'error_msg' : txt })

@login_required
def import_team(request):
    if request.method == 'POST':
        form = ImportForm(request.POST)
        form1 = RegisterForm(request.POST)
        if form.is_valid():
            model=Import(**form.cleaned_data)
            model.author = request.user
            model.save()
            return render_to_response('register-team.html', { 'form' : form1, 'username' : request.user.username } )
    else:
        if 'last_event' in request.GET:
            last_event = upper(request.GET ['last_event'])
            if rbtx_is_valid_event_code(last_event):
                form = ImportForm(initial = {'event' : last_event})
                form1 = RegisterForm(initial = {'event' : last_event})
            else:
                form1 = RegisterForm()
                form = ImportForm()
        else:
            form = ImportForm()
            form1 = RegisterForm()
    return render_to_response('import-team.html', { 'form' : form, 'username' : request.user.username })

@login_required
def register_team(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form1 = ImportForm(request.POST)
        if form1.is_valid():
            model=Import(**form1.cleaned_data)
            model.author = request.user
            model.save()
            rnum = model.ref_num
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=TeamName')
            teamName = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Event')
            eventName = req.read() 
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=College1')
            #college1 = req.read()
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=College2')
            #college2 = req.read()
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=College3')
            #college3 = req.read()
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=College4')
            #college4 = req.read()
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Contact1')
            #contact1 = req.read()
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Contact2')
            #contact2 = req.read()
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Contact3')
            #contact3 = req.read()
            #req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Contact4')
            #contact4 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Email1')
            email1 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Email2')
            email2 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Email3')
            email3 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Email4')
            email4 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=First')
            name1 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Second')
            name2 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Third')
            name3 = req.read()
            req = urllib2.urlopen('http://robotix.in/registration/searchreq.php?team='+rnum+'&prop=Fourth')
            name4 = req.read()
            form = RegisterForm(initial=  {'team_name':teamName, 'event':eventName, 'email_a': email1, 'email_b': email2, 'email_c': email3, 'email_d': email4, 'participant_1':name1, 'participant_2': name2 ,'participant_3': name3, 'participant_4': name4 })

            return render_to_response('register-team.html', { 'form' : form, 'username' : request.user.username } )
        #   return render_to_response('register-team.html', {'importform' : importform, 'username' : request.user.username })
        if form.is_valid():
            model = Team (**form.cleaned_data)
            model.author = request.user
            model.save()
            team_id = model.assign_team_id()
            return render_to_response('post-registration.html',
                                      { 'team_id' : team_id,
                                        'event_code' : model.event,
                                        'event' : rbtx_event_code_to_event_name(model.event),
                                        'team_name' : model.team_name,
                                        'username' : request.user.username})
    else:
        if 'last_event' in request.GET:
            last_event = upper(request.GET ['last_event'])
            if rbtx_is_valid_event_code(last_event):
                form = RegisterForm(initial = {'event' : last_event})
                form1 = ImportForm(initial = {'event' : last_event})
            else:
                form = RegisterForm()
                form1 = ImportForm()
        else:
            form = RegisterForm()
            form1 = ImportForm() 
    return render_to_response('import-team.html', { 'form' : form1, 'username' : request.user.username })

@login_required
def retrieve_team_information(request, team_id):
    team = rbtx_find_team_by_id(team_id)
    if team:
        return render_to_response('team-info.html', { 'team' : team, 'username' : request.user.username })
    else:
        return _construct_err('Could not locate information about team \'' + team_id + '\'')

def retrieve_basic_team_information(request, team_id):
    team = rbtx_find_team_by_id(team_id)
    if team:
        return render_to_response('team-info-basic.html', { 'team' : team, 'username' : request.user.username })
    else:
        return _construct_err('Could not locate information about team \'' + team_id + '\'')

@login_required
def retrieve_list_of_registered_teams(request, event_code):
    event_code = upper(event_code)
    event_name = rbtx_event_code_to_event_name(event_code)
    if event_code == 'ALL':
        return render_to_response('teams-list.html', { 'event_name' : 'all events',
                                                       'event_code' : '',
                                                       'date_time' : datetime.now(),
                                                       'teams' : Team.objects.all(),
                                                       'username' : request.user.username} )
    elif rbtx_is_valid_event_code(event_code):
        return render_to_response('teams-list.html', { 'event_name' : event_name,
                                                       'event_code' : event_code,
                                                       'date_time' : datetime.now(),
                                                       'teams' : Team.objects.filter(event = event_code),
                                                       'username' : request.user.username})
    else:
        return _construct_err('\'' + str(event_code) + '\' is not an event code.')

def _is_overwriting(model_cls, form_data):
    x = model_cls.objects.filter(team = form_data ['team'])
    if len(x) == 0:
        return None
    else:
        return x[0]

def _has_scored_before(model_cls, team):
    x = model_cls.objects.filter(team = team)
    if len(x) == 0:
        return None
    else:
        return x[0]

def estimate_score(request, event_code, round_no):
    model_cls = rbtx_get_model_class_by_code_and_round(event_code, round_no)

    if model_cls is None:
        return HttpResponse("0")

    if request.method == 'GET':
        fresh_data = {}
        for (k, v) in request.GET.items():
            fresh_data [k] = int(v)
        model = model_cls(**fresh_data)
        return HttpResponse(str(model.calculate_score()))
    return HttpResponse("")

@login_required
def master_judge(request, event_code, round_no, team_id):
    """
    This is a generic method which judges *all* the events.
    Note: team_id is the id of team being evaluated. It may be None, in which case we 
    present a default view.
    """

    re_editing = False
    team = None
    # First try to locate the classes.
    form_cls = rbtx_get_form_class_by_code_and_round(event_code, round_no)
    model_cls = rbtx_get_model_class_by_code_and_round(event_code, round_no)

    if form_cls is None:
        return _construct_err('Could not find form class for %s / %s' % (event_code, round_no))
    if model_cls is None:
        return _construct_err('Could not find model class for %s / %s' % (event_code, round_no))

    if request.method == 'POST':
        form = form_cls(request.POST)
        if form.is_valid():
            # Now check if we're over-writing something ... 
            data = form.cleaned_data
            tmp_model = _is_overwriting(model_cls, data)
            model = model_cls(**data)
            print data
            if tmp_model:
                # ... then so be it!
                model.id = tmp_model.id
                model.conducted_on = datetime.now()
            model.author = request.user
            model.save()
            model.team.save()
            return render_to_response('scoring-done.html', { 'team_id' : model.team.get_decorated_team_id (),
                                                             'score' : model.edited_score,
                                                             'time' : model.conducted_on,
                                                             'edited' : model.edited_score != model.calculate_score (),
                                                             'original_score' : model.calculate_score (),
                                                             'event_name' : rbtx_event_code_to_event_name(event_code),
                                                             'event_code' : event_code,
                                                             'round_no' : round_no,
                                                             'username' : request.user.username})
    else:
        # If team_id is None in a non POST request, then simply display a default form.
        if team_id == 'XX0':
            form = form_cls()
        else:
            # Now we need to actually look for the team with id team_id, and set fields
            # accordingly.
            team = rbtx_find_team_by_id(team_id)
            # Check if we've scored this team before ... 
            x = _has_scored_before(model_cls, team)
            if x:
                # ... if yes, awesome.
                form = form_cls(initial = model_to_dict(x))
                re_editing = True
            else:
                # ... otherwise just set the select box.
                form = form_cls(initial = {'team' : team})

    return render_to_response('judge.html', { 'form' : form,
                                              'event_name' : rbtx_event_code_to_event_name(event_code),
                                              'event_code' : event_code,
                                              'round_no'   : round_no,
                                              'username' : request.user.username,
                                              're_editing' : re_editing,
                                              'team' : team})

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html', {})


def root(request):
    return render_to_response('index.html', {})

@login_required
def best_algorithm_design(request):
    lst = rbtx_get_model_list()
    result = []
    for x in lst:
        k = x.objects.filter(best_algorithm_design = True)
        for y in k:
            result = result + [ y.team ]
    return render_to_response('best.html', { 'what' : 'algorithm',
                                             'result' : result})

@login_required
def best_mechanical_design(request):
    lst = rbtx_get_model_list()
    result = []
    for x in lst:
        k = x.objects.filter(best_algorithm_design = True)
        for y in k:
            result = result + [ y.team ]
    return render_to_response('best.html', { 'what' : 'mechanical',
                                             'result' : result})

@login_required
def timer(request):
    return render_to_response('timer.html')

@login_required
def score_board(request, event_code, round_no):
    model_cls = rbtx_get_model_class_by_code_and_round(event_code, round_no)
    if not model_cls:
        return _construct_err('Could not find model for %s / %s' % (event_code, round_no))
    event_name = rbtx_event_code_to_event_name(event_code)
    return render_to_response('score-board.html', { 'models' : model_cls.objects.order_by('-edited_score'),
                                                    'event_name' : event_name,
                                                    'round_no' : round_no })

def _construct_could_not_find_err(event_code, r_no):
    return _construct_err('Could not find event with code ' + event_code + '/' + str(r_no))

def _process_promotion(prom_form, model_cls, src_round):
    ret = []
    for t in model_cls.objects.all():
        if prom_form.cleaned_data[t.team.get_decorated_team_id()]:
            t.team.promoted_to = src_round + 1
            t.team.save()
            ret.append(t.team)
        else:
            t.team.promoted_to = src_round
            t.team.save()
    return ret

@login_required
def promotion_interface(request, event, from_round):
    model_cls = rbtx_get_model_class_by_code_and_round(event, from_round)
    
    if not model_cls:
        return _construct_could_not_find_err(event, from_round)

    if request.method == 'POST':
        form_cls = rbtx_make_promotion_form(model_cls.objects.all().order_by('-edited_score'), int(from_round))
        f_real = form_cls(request.POST)
        if f_real.is_valid():
            teams = _process_promotion(f_real, model_cls, int(from_round))
            return render_to_response('promoted.html', {
                    'teams' : teams,
                    'from_round' : from_round,
                    'to_round' : int(from_round) + 1,
                    'event_name' : rbtx_event_code_to_event_name(event),
                    'event_code': event})
    else:
        f_real = rbtx_make_promotion_form(model_cls.objects.all().order_by('-edited_score'), int(from_round))()

    return render_to_response('promotion.html', {
            'form_real' : f_real,
            'event_name' : rbtx_event_code_to_event_name(event),
            'event_code' : event,
            'from_round' : from_round,
            'to_round' : (int(from_round) + 1)});

@login_required
def teams_not_scored(request, event, round_no):
    model_cls = rbtx_get_model_class_by_code_and_round(event, round_no)
    teams = Team.objects.filter(event = event)
    lst = []
    for t in teams:
        if len(model_cls.objects.filter(team = t)) == 0:
            lst.append(t)
    return render_to_response('not-scored.html', {'teams' : lst,
                                                  'round_no' : round_no})
