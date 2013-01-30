from django import forms
from django.utils.datastructures import SortedDict

from eventmanager.models import *
from eventmanager.view_utils import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Team

_common_fields = ('edited_score', 'best_algorithm_design', 'best_mechanical_design', 'comments')

class StalkerFirstRoundForm(forms.ModelForm):
    class Meta:
        model = StalkerFirstRound
        fields = ('team', 'checkpoints_detected', 'complete_marker_passes', 'partial_marker_passes',
                  'max_time_to_be_allotted', 'num_restarts', 'num_timeouts', 'time_taken') + _common_fields

class StalkerSecondRoundForm(forms.ModelForm):
    class Meta:
        model = StalkerSecondRound
        fields = ('team', 'checkpoints_detected', 'complete_marker_passes', 'partial_marker_passes',
                  'max_time_to_be_allotted', 'num_restarts', 'num_timeouts', 'time_taken') + _common_fields

class StalkerThirdRoundForm(forms.ModelForm):
    class Meta:
        model = StalkerThirdRound
        fields = ('team', 'checkpoints_detected', 'complete_marker_passes', 'partial_marker_passes',
                  'max_time_to_be_allotted', 'num_restarts', 'num_timeouts', 'time_taken') + _common_fields


class InfernoFirstRoundForm(forms.ModelForm):
    class Meta:
        model = InfernoFirstRound
        fields = ('team', 'black_cylinders', 'white_cylinders', 'candles_put_out', 'cylinders_in_safe_zone',
                  'fires_touched', 'fires_dropped', 'cylinder_in_contact_with_candle', 'restarts', 'timeouts', 'time_taken') + _common_fields

class InfernoSecondRoundForm(forms.ModelForm):
    class Meta:
        model = InfernoSecondRound
        fields = ('team', 'black_cylinders', 'white_cylinders', 'candles_put_out', 'cylinders_in_safe_zone', 
                  'fires_touched', 'fires_dropped', 'cylinder_in_contact_with_candle', 'restarts', 'timeouts', 'time_taken') + _common_fields

class InfernoThirdRoundForm(forms.ModelForm):
    class Meta:
        model = InfernoThirdRound
        fields = ('team', 'black_cylinders', 'white_cylinders', 'candles_put_out', 'cylinders_in_safe_zone',
                  'fires_touched', 'fires_dropped', 'cylinder_in_contact_with_candle', 'restarts', 'timeouts', 'time_taken') + _common_fields

class VertigoFirstRoundForm(forms.ModelForm):
    class Meta:
        model = VertigoFirstRound
        fields = ('team', 'cylinder1_red_zone_15', 'cylinder2_red_zone_15', 'cylinder3_red_zone_15', 'cylinder4_red_zone_15',
                  'cylinder1_yellow_zone_10', 'cylinder2_yellow_zone_10', 'cylinder3_yellow_zone_10', 'cylinder4_yellow_zone_10',
                  'cylinder1_green_zone_5', 'cylinder2_green_zone_5', 'cylinder3_green_zone_5', 'cylinder4_green_zone_5',
                  'time_taken', 'self_clasping_mechanism_bonus', 'one_bounce_out_partial_score','restarts','timeouts',
                  'outside_penalty', 'bot_falling_off_the_zipline_penalty', 'refill_penalty') + _common_fields

class VertigoSecondRoundForm(forms.ModelForm):
    class Meta:
        model = VertigoSecondRound
        fields = ('team', 'cylinder1_red_zone_15', 'cylinder2_red_zone_15', 'cylinder3_red_zone_15', 'cylinder4_red_zone_15',
                  'cylinder1_yellow_zone_10', 'cylinder2_yellow_zone_10', 'cylinder3_yellow_zone_10', 'cylinder4_yellow_zone_10',
                  'cylinder1_green_zone_5', 'cylinder2_green_zone_5', 'cylinder3_green_zone_5', 'cylinder4_green_zone_5',
                  'clampings_done_right', 'bot_falling_off_after_clamping',     
                  'time_taken', 'self_clasping_mechanism_bonus', 'one_bounce_out_partial_score','restarts','timeouts',
                  'outside_penalty', 'bot_falling_off_the_zipline_penalty', 'refill_penalty') + _common_fields

class VertigoThirdRoundForm(forms.ModelForm):
    class Meta:
        model = VertigoThirdRound
        fields = ('team', 'cylinder1_red_zone_15', 'cylinder2_red_zone_15', 'cylinder3_red_zone_15', 'cylinder4_red_zone_15',
                  'cylinder1_yellow_zone_10', 'cylinder2_yellow_zone_10', 'cylinder3_yellow_zone_10', 'cylinder4_yellow_zone_10',
                  'cylinder1_green_zone_5', 'cylinder2_green_zone_5', 'cylinder3_green_zone_5', 'cylinder4_green_zone_5',
                  'clampings_done_right', 'bot_falling_off_after_clamping',  
                  'time_taken', 'self_clasping_mechanism_bonus', 'one_bounce_out_partial_score','restarts','timeouts',
                  'outside_penalty', 'bot_falling_off_the_zipline_penalty', 'refill_penalty') + _common_fields

class StasisFirstRoundForm(forms.ModelForm):
    class Meta:
        model = StasisFirstRound
        fields = ('team', 'd_speed_breakers', 'd_uneven_speed_breakers', 'd_steps', 'd_hill', 'd_incline',
                  'd_wedge', 'd_bend', 'y_water_outer_tumbler', 'num_restarts', 'num_timeouts', 
                  'fully_autonomous', 'semi_autonomous', 'time_taken') + _common_fields  

class StasisSecondRoundForm(forms.ModelForm):
    class Meta:
        model = StasisSecondRound
        fields = ('team', 'd_speed_breakers', 'd_uneven_speed_breakers', 'd_steps', 'd_hill', 'd_incline',
                  'd_wedge', 'd_bend', 'y_water_outer_tumbler', 'num_restarts', 'num_timeouts', 
                  'fully_autonomous', 'semi_autonomous', 'time_taken') + _common_fields

class StasisThirdRoundForm(forms.ModelForm):
    class Meta:
        model = StasisThirdRound
        fields = ('team', 'd_speed_breakers', 'd_uneven_speed_breakers', 'd_steps', 'd_hill', 'd_incline',
                  'd_wedge', 'd_bend', 'y_water_outer_tumbler', 'num_restarts', 'num_timeouts', 
                  'fully_autonomous', 'semi_autonomous', 'time_taken') + _common_fields
'''
class NukeClearFirstRoundForm(forms.ModelForm):
    class Meta:
        model = NukeClearFirstRound
        fields = ('team', 'time_taken', 'score') + _common_fields

class NukeClearSecondRoundForm(forms.ModelForm):
    class Meta:
        model = NukeClearSecondRound
        fields = ('team', 'time_taken', 'score') + _common_fields

class NukeClearThirdRoundForm(forms.ModelForm):
    class Meta:
        model = NukeClearThirdRound
        fields = ('team', 'time_taken', 'score') + _common_fields  '''
 

def rbtx_get_form_class_by_code_and_round(code, rnd):
    """ rbtx_get_form_class_by_code_and_round ('IN', 2) will return InfernoSecondRoundForm etc. """
    if not rbtx_is_valid_event_code(code):
        return None
    code = upper(code)

    try:
        rnd = int(rnd)
    except ValueError:
        return None
    
    if code == 'ST':
        if rnd == 1:
            return StalkerFirstRoundForm
        elif rnd == 2:
            return StalkerSecondRoundForm
        elif rnd == 3:
            return StalkerThirdRoundForm
    elif code == 'IN':
        if rnd == 1:
            return InfernoFirstRoundForm
        elif rnd == 2:
            return InfernoSecondRoundForm
        elif rnd == 3:
            return InfernoThirdRoundForm
    elif code == 'VT':
        if rnd == 1:
            return VertigoFirstRoundForm
        elif rnd == 2:
            return VertigoSecondRoundForm
        elif rnd == 3:
            return VertigoThirdRoundForm
    elif code == 'NC':
        if rnd == 1:
            return NukeClearFirstRoundForm
        elif rnd == 2:
            return NukeClearSecondRoundForm
    elif code == 'SS':
        if rnd == 1:
            return StasisFirstRoundForm
        elif rnd == 2:
            return StasisSecondRoundForm
        elif rnd ==3:
            return StasisThirdRoundForm
    return None
    '''if code == 'RA':
        if rnd == 1:
            return RaftFirstRoundForm
        elif rnd == 2:
            return RaftSecondRoundForm
    elif code == 'BL':
        if rnd == 1:
            return BallistaFirstRoundForm
        elif rnd == 2:
            return BallistaSecondRoundForm
        elif rnd == 3:
            return BallistaThirdRoundForm
    elif code == 'PB':
        if rnd == 1:
            return PirateBayFirstRoundForm
        elif rnd == 2:
            return PirateBaySecondRoundForm
        elif rnd == 3:
            return PirateBayThirdRoundForm
    elif code == 'FG':
        if rnd == 1:
            return FugitivesFirstRoundForm
    elif code == 'AS':
        if rnd == 1:
            return ASMEFirstRoundForm
    elif code == 'RC':
        if rnd == 1:
            return RobocopFirstRoundForm
        elif rnd == 2:
            return RobocopSecondRoundForm
    return None
'''
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
