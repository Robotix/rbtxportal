from django import forms
from django.utils.datastructures import SortedDict

from eventmanager.models import *
from eventmanager.view_utils import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Team

#class ImportForm(forms.ModelForm):
#   class Meta:
#      model = Import

_common_fields = ('edited_score', 'best_algorithm_design', 'best_mechanical_design', 'comments')

class LumosFirstRoundForm(forms.ModelForm):
    class Meta:
        model = LumosFirstRound
        fields = ('team', 'stationaryLight_deactivated', 'movingLight_deactivated', 'incorrect_source',
                   'num_restarts', 'num_timeouts','max_time_to_be_allotted', 'time_taken') + _common_fields

class LumosSecondRoundForm(forms.ModelForm):
    class Meta:
        model = LumosSecondRound
        fields = ('team', 'stationaryLight_deactivated', 'movingLight_deactivated', 'incorrect_source',
                   'num_restarts', 'num_timeouts','max_time_to_be_allotted', 'time_taken') + _common_fields

class LumosThirdRoundForm(forms.ModelForm):
    class Meta:
        model = LumosThirdRound
        fields = ('team', 'stationaryLight_deactivated', 'movingLight_deactivated', 'incorrect_source',
                   'num_restarts', 'num_timeouts','max_time_to_be_allotted', 'time_taken') + _common_fields

class OverhaulFirstRoundForm(forms.ModelForm):
    class Meta:
        model = OverhaulFirstRound
        fields = ('team', 'successful_bridging', 'safe_zone', 'joints_dropped', 'bot_fallen',
                  'time_taken','timeouts', 'restarts') + _common_fields

class OverhaulSecondRoundForm(forms.ModelForm):
    class Meta:
        model = OverhaulSecondRound
        fields = ('team', 'successful_bridging', 'victim_picked_firstChk', 'victim_picked_secondChk', 'victim_picked_thirdChk', 
                  'red_victims', 'yellow_victims', 'green_victims', 'victims_dropped', 'joints_dropped', 'bot_fallen', 'time_taken', 'timeouts', 'restarts') + _common_fields

class OverhaulThirdRoundForm(forms.ModelForm):
    class Meta:
        model = OverhaulThirdRound
        fields = ('team', 'successful_bridging', 'victim_picked_firstChk', 'victim_picked_secondChk', 'victim_picked_thirdChk', 
                  'red_victims', 'yellow_victims', 'green_victims', 'victims_dropped', 'joints_dropped', 'bot_fallen', 'time_taken', 'timeouts', 'restarts') + _common_fields

class AbyssFirstRoundForm(forms.ModelForm):
    class Meta:
        model = AbyssFirstRound
        fields = ('team', 'pick_green', 'deposited_rings', 'damage_done',
                  'time_taken', 'restarts', 'timeouts') + _common_fields

class AbyssSecondRoundForm(forms.ModelForm):
    class Meta:
        model = AbyssSecondRound
        fields = ('team', 'pick_green', 'deposited_rings', 'red_collected', 'damage_done',
                  'time_taken', 'restarts', 'timeouts') + _common_fields

class AbyssThirdRoundForm(forms.ModelForm):
    class Meta:
        model = AbyssThirdRound
        fields = ('team', 'pick_green', 'deposited_rings', 'red_collected', 'damage_done',
                  'time_taken', 'restarts', 'timeouts') + _common_fields

class ACROSSFirstRoundForm(forms.ModelForm):
    class Meta:
        model = ACROSSFirstRound
        fields = ('team', 'lower_correct_position', 'sense_gap', 'collision_blocker', 'collision_building', 'grids_crossed',
                  'num_restarts', 'num_timeouts', 'time_taken' ) + _common_fields  

class ACROSSSecondRoundForm(forms.ModelForm):
    class Meta:
        model = ACROSSSecondRound
        fields = ('team', 'lower_correct_position', 'sense_gap', 'collision_blocker', 'collision_building', 'grids_crossed',
                  'num_restarts', 'num_timeouts', 'time_taken' ) + _common_fields  

class ACROSSThirdRoundForm(forms.ModelForm):
    class Meta:
        model = ACROSSThirdRound
        fields = ('team', 'lower_correct_position', 'sense_gap', 'collision_blocker', 'collision_building', 'grids_crossed',
                  'num_restarts', 'num_timeouts', 'time_taken' ) + _common_fields  

class SeekerFirstRoundForm(forms.ModelForm):
    class Meta:
        model = SeekerFirstRound
        fields = ('team', 'correct_turn', 'stop_end', 'time_taken', 'wall_hits', 'restarts','time_outs_taken') + _common_fields

class SeekerSecondRoundForm(forms.ModelForm):
    class Meta:
        model = SeekerSecondRound
        fields = ('team', 'correct_turn', 'stop_end', 'time_taken', 'wall_hits', 'restarts','time_outs_taken') + _common_fields

class SeekerThirdRoundForm(forms.ModelForm):
    class Meta:
        model = SeekerThirdRound
        fields = ('team', 'correct_turn', 'stop_end', 'time_taken', 'wall_hits','correct_zone', 'wrong_zone', 'restarts','time_outs_taken') + _common_fields

def rbtx_get_form_class_by_code_and_round(code, rnd):
    """ rbtx_get_form_class_by_code_and_round ('OV', 2) will return OverhaulSecondRoundForm etc. """
    if not rbtx_is_valid_event_code(code):
        return None
    code = upper(code)

    try:
        rnd = int(rnd)
    except ValueError:
        return None
    
    if code == 'LU':
        if rnd == 1:
            return LumosFirstRoundForm
        elif rnd == 2:
            return LumosSecondRoundForm
        elif rnd == 3:
            return LumosThirdRoundForm
    elif code == 'OV':
        if rnd == 1:
            return OverhaulFirstRoundForm
        elif rnd == 2:
            return OverhaulSecondRoundForm
        elif rnd == 3:
            return OverhaulThirdRoundForm
    elif code == 'AB':
        if rnd == 1:
            return AbyssFirstRoundForm
        elif rnd == 2:
            return AbyssSecondRoundForm
        elif rnd == 3:
            return AbyssThirdRoundForm
    elif code == 'SE':
        if rnd == 1:
            return SeekerFirstRoundForm
        elif rnd == 2:
            return SeekerSecondRoundForm
        elif rnd == 3:
            return SeekerThirdRoundForm
    elif code == 'AC':
        if rnd == 1:
            return ACROSSFirstRoundForm
        elif rnd == 2:
            return ACROSSSecondRoundForm
        elif rnd ==3:
            return ACROSSThirdRoundForm
    return None
   
def rbtx_make_promotion_form(models, src_round):
    fields = SortedDict()
    i = 1
    for model in models:
        x = False
        if model.team.promoted_to == src_round + 1:
            msg = str (i) + ". " + str(model.team) + ' - ' + str(model.edited_score) + ' points (College: ' + model.team.college + ')'
            x = True
        elif model.team.promoted_to == src_round:
            msg = str (i) + ". " + str(model.team) + ' - ' + str(model.edited_score) + ' points (College: ' + model.team.college + ')'
        else:
            continue
        fields [model.team.get_decorated_team_id ()] = forms.BooleanField(label = msg, required = False,
                                                                          initial = x,
                                                                          help_text = '<a href="/info/' + model.team.get_decorated_team_id() + '" target="blank_">info</a>')
        fields.keyOrder.append(model.team.get_decorated_team_id ())
        i = i + 1
    return type('PromotionForm', (forms.BaseForm,), { 'base_fields' : fields} )
