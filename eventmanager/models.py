from django.db import models
from string import upper
from django.contrib.auth.models import User

EVENT_CHOICES = (
    ('LU', 'Lumos'),
    ('OV', 'Overhaul'),
    ('AB', 'Abyss'),
    ('SE', 'Seeker'),
    ('AC', 'ACROSS'),
)

def rbtx_event_code_to_event_name(code):
    """ Return the event name corresponding to the event code code. """
    code = upper(code)
    for x in EVENT_CHOICES:
        if x [0] == code:
            return x [1]

def rbtx_is_valid_event_code(code):
    """ Check if code corresponds to a valid event code. """
    code = upper(code)
    for x in EVENT_CHOICES:
        if x [0] == code:
            return True
    return False

#class Import(models.Model):
 #   ref_num = models.IntegerField(blank = True, verbose_name='Reference Number:')

class Team(models.Model):
    """ Represents one team, to take part in one event. """

    team_name = models.CharField(max_length = 255, verbose_name = 'Team Name')
    author = models.ForeignKey(User, editable = False)

    # Event specific ID
    team_id = models.IntegerField(blank = True, verbose_name = 'Team ID', editable = False, default = 0)
    event = models.CharField(max_length = 2, choices = EVENT_CHOICES, verbose_name = 'Event')

    college = models.CharField(max_length = 255, verbose_name = 'College')
    number_a = models.CharField(max_length = 15, verbose_name = 'Primary Contact Number')
    number_b = models.CharField(max_length = 15, blank = True, verbose_name = 'Secondary Contact Number')
    email = models.EmailField(verbose_name = 'Contact Email', blank = True)

    participant_1 = models.CharField(max_length = 255, verbose_name = 'First Participant')
    participant_2 = models.CharField(max_length = 255, blank = True, verbose_name = 'Second Participant')
    participant_3 = models.CharField(max_length = 255, blank = True, verbose_name = 'Third Participant')
    participant_4 = models.CharField(max_length = 255, blank = True, verbose_name = 'Fourth Participant')

    registered_on = models.DateTimeField(auto_now_add = True)

    comments = models.TextField(blank = True)

    promoted_to = models.IntegerField(blank = True, editable = False, default = 1)
    best_mechanical_design = models.BooleanField(default = False, editable = False)
    best_algorithm_design = models.BooleanField(default = False, editable = False)

    def __unicode__(self):
        return self.get_decorated_team_id() + ' (' + self.team_name + ')'

    def assign_team_id(self):
        """ Assign a event-unique team ID to the object """
        objects = Team.objects.filter(event = self.event)
        if len(objects) == 0:
            self.team_id = 1
        else:
            self.team_id = objects.aggregate(models.Max('team_id')) ['team_id__max'] + 1
        self.save ()
        return self.get_decorated_team_id()

    def get_decorated_team_id(self):
        """ Get the decorated team ID, of the form RA123 """
        return self.event + str(self.team_id)

class _EventBase(models.Model):
    """ An abstract model describing the features common to all the event models. """

    author = models.ForeignKey(User, editable = False)
    comments = models.TextField(blank = True)
    edited_score = models.IntegerField(verbose_name = 'Score')
    conducted_on = models.DateTimeField(auto_now_add = True)
    best_algorithm_design = models.BooleanField(default = False)
    best_mechanical_design = models.BooleanField(default = False)

    class Meta:
        abstract = True

class LumosFirstRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = {'event__exact': 'LU', 'promoted_to__exact' : 1 })
    
    stationaryLight_deactivated = models.IntegerField(verbose_name = 'Number of Stationary Light Sources Deactivated:')
    movingLight_deactivated = models.IntegerField(verbose_name = 'Number of Moving Light Sources Deactivated:')
    incorrect_source=models.IntegerField(verbose_name='Number of times bot hits deactivated source:')
    num_restarts = models.IntegerField(verbose_name = 'Number of Restarts:')
    num_timeouts = models.IntegerField(verbose_name = 'Number of Time-Outs:')
    max_time_to_be_allotted = models.IntegerField(verbose_name = 'Alotted Run-Time(in s):')
    time_taken = models.IntegerField()

    def calculate_score(self):
        score = 0 
        score = score + 80 * self.stationaryLight_deactivated
        score = score + 120 * self.movingLight_deactivated
        score = score - 75 * self.incorrect_source 
        score = score - 50 * self.num_restarts
        score = score - 20 * self.num_timeouts
        if self.max_time_to_be_allotted > self.time_taken:
	       score = score + ((self.max_time_to_be_allotted-self.time_taken)/2)
        return score

    def __unicode__(self):
        return 'First Lumos round for team \'' + str(self.team) + '\''

class LumosSecondRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = {'event__exact': 'LU', 'promoted_to__exact' : 2 })

    checkpoints_detected = models.IntegerField(verbose_name = 'Number of checkpoints detected')
    stationaryLight_deactivated = models.IntegerField(verbose_name = 'Number of Stationary Light Sources Deactivated:')
    movingLight_deactivated = models.IntegerField(verbose_name = 'Number of Moving Light Sources Deactivated:')
    incorrect_source=models.IntegerField(verbose_name='Number of times bot hits deactivated source:')
    num_restarts = models.IntegerField(verbose_name = 'Number of Restarts:')
    num_timeouts = models.IntegerField(verbose_name = 'Number of Time-Outs:')
    max_time_to_be_allotted = models.IntegerField(verbose_name = 'Alotted Run-Time(in s)')
    time_taken = models.IntegerField()

    def calculate_score(self):
        score = 0 
        score = score + 80 * self.stationaryLight_deactivated
        score = score + 120 * self.movingLight_deactivated
        score = score - 75 * self.incorrect_source 
        score = score - 50 * self.num_restarts
        score = score - 20 * self.num_timeouts
        if self.max_time_to_be_allotted > self.time_taken:
	       score = score + ((max_time_to_be_allotted-time_taken)/2)
        return score

    def __unicode__(self):
        return 'Second Lumos round for team \'' + str(self.team) + '\''

class LumosThirdRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = {'event__exact': 'LU', 'promoted_to__exact' : 3 })

    stationaryLight_deactivated = models.IntegerField(verbose_name = 'Number of Stationary Light Sources Deactivated:')
    movingLight_deactivated = models.IntegerField(verbose_name = 'Number of Moving Light Sources Deactivated:')
    incorrect_source=models.IntegerField(verbose_name='Number of times bot hits deactivated source:')
    num_restarts = models.IntegerField(verbose_name = 'Number of Restarts:')
    num_timeouts = models.IntegerField(verbose_name = 'Number of Time-Outs:')
    max_time_to_be_allotted = models.IntegerField(verbose_name = 'Alotted Run-Time(in s)')
    time_taken = models.IntegerField()

    def calculate_score(self):
        score = 0 
        score = score + 80 * self.stationaryLight_deactivated
        score = score + 120 * self.movingLight_deactivated
        score = score - 75 * self.incorrect_source 
        score = score - 50 * self.num_restarts
        score = score - 20 * self.num_timeouts
        if self.max_time_to_be_allotted > self.time_taken:
	       score = score + ((max_time_to_be_allotted-time_taken)/2)
        return score

class OverhaulFirstRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'OV', 'promoted_to__exact' : 1 })
    
    successful_bridging = models.IntegerField(verbose_name = 'Number of successful bridging:')
    safe_zone = models.IntegerField(verbose_name = 'Robot in safe zone(0 if No 1 if Yes):')
    joints_dropped = models.IntegerField(verbose_name = 'Number of joints dropped:')
    bot_fallen = models.IntegerField(verbose_name = 'Number of times Bot fell off: ')
    time_taken = models.IntegerField(verbose_name = 'Time taken:')
    timeouts = models.IntegerField(verbose_name = 'Number of time-outs taken:')
    restarts = models.IntegerField(verbose_name = 'Number of restarts taken:')

    def calculate_score(self):
        score = 0
        score = score + 150 * self.successful_bridging
        score = score + 100 * self.safe_zone
        score = score - 30 * self.joints_dropped
        score = score - 50 * self.bot_fallen
        score = score - 50 * self.timeouts
        score = score - 100 * self.restarts 
        if self.time_taken < 180:
            score = score + (180-self.time_taken)
        return score

    def __unicode__(self):
        return 'First Overhaul round for team \'' + str(self.team) + '\''

class OverhaulSecondRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'OV', 'promoted_to__exact' : 2 })
    
    successful_bridging = models.IntegerField(verbose_name = 'Number of successful bridging:')
    victim_picked_firstChk = models.IntegerField(verbose_name = 'Number of victims picked at Checkpoint 1:')
    victim_picked_secondChk = models.IntegerField(verbose_name = 'Number of victims picked at Checkpoint 2:')
    victim_picked_thirdChk = models.IntegerField(verbose_name = 'Number of victims picked at Checkpoint 3:')
    red_victims = models.IntegerField(verbose_name = 'Number of red victims saved:')
    yellow_victims = models.IntegerField(verbose_name = 'Number of yellow victims saved:')
    green_victims = models.IntegerField(verbose_name = 'Number of green victims saved:')
    victims_dropped = models.IntegerField(verbose_name = 'Number of victims dropped:')
    joints_dropped = models.IntegerField(verbose_name = 'Number of joints dropped:')
    bot_fallen = models.IntegerField(verbose_name = 'Number of times Bot fell off: ')
    time_taken = models.IntegerField(verbose_name = 'Time taken:')
    timeouts = models.IntegerField(verbose_name = 'Number of time-outs taken:')
    restarts = models.IntegerField(verbose_name = 'Number of restarts taken:')

    def calculate_score(self):
        score = 0
        score = score + 150 * self.successful_bridging
        score = score + 25 * self.victim_picked_firstChk
        score = score + 25 * self.victim_picked_secondChk
        score = score + 25 * self.victim_picked_thirdChk
        score = score + 100 * self.red_victims
        score = score + 75 * self.yellow_victims
        score = score + 50 * self.green_victims
        score = score - 30 * self.joints_dropped
        score = score - 50 * self.bot_fallen
        score = score - 50 * self.timeouts
        score = score - 40 * self.victims_dropped
        score = score - 100 * self.restarts 
        if self.time_taken < 240:
            score = score + (240-self.time_taken)
        return score

    def __unicode__(self):
        return 'Second Overhaul Round for Team \'' + str(self.team) + '\''

class OverhaulThirdRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'OV', 'promoted_to__exact' : 3 })
    
    successful_bridging = models.IntegerField(verbose_name = 'Number of successful bridging:')
    victim_picked_firstChk=models.IntegerField(verbose_name = 'Number of victims picked at Checkpoint 1:')
    victim_picked_secondChk=models.IntegerField(verbose_name = 'Number of victims picked at Checkpoint 2:')
    victim_picked_thirdChk=models.IntegerField(verbose_name = 'Number of victims picked at Checkpoint 3:')
    red_victims = models.IntegerField(verbose_name = 'Number of red victims saved:')
    yellow_victims = models.IntegerField(verbose_name = 'Number of yellow victims saved:')
    green_victims = models.IntegerField(verbose_name = 'Number of green victims saved:')
    victims_dropped = models.IntegerField(verbose_name = 'Number of victims dropped:')
    joints_dropped = models.IntegerField(verbose_name = 'Number of joints dropped:')
    bot_fallen = models.IntegerField(verbose_name = 'Number of times Bot fell off: ')
    time_taken = models.IntegerField(verbose_name = 'Time taken:')
    timeouts = models.IntegerField(verbose_name = 'Number of time-outs taken:')
    restarts = models.IntegerField(verbose_name = 'Number of restarts taken:')

    def calculate_score(self):
        score = 0
        score = score + 150 * self.successful_bridging
        score = score + 25 * self.victim_picked_firstChk
        score = score + 25 * self.victim_picked_secondChk
        score = score + 25 * self.victim_picked_thirdChk
        score = score + 100 * self.red_victims
        score = score + 75 * self.yellow_victims
        score = score + 100 * self.green_victims
        score = score - 30 * self.joints_dropped
        score = score - 50 * self.bot_fallen
        score = score - 50 * self.timeouts
        score = score - 40 * self.victims_dropped
        score = score - 100 * self.restarts 
        if self.time_taken < 240:
            score = score + (240-self.time_taken)
        return score

    def __unicode__(self):
        return 'Third Overhaul round for team \'' + str(self.team) + '\''

class AbyssFirstRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'AB', 'promoted_to__exact' : 1 })

    pick_green = models.IntegerField(verbose_name = 'Number of green rings picked:')
    deposited_rings = models.IntegerField(verbose_name = 'Number of rings deposited:')
    #red_collected = models.IntegerField(verbose_name = 'Number of red rings collected:')
    damage_done = models.IntegerField(verbose_name = 'Number of Damages:') 
    time_taken = models.IntegerField(verbose_name = 'Time taken')
    restarts = models.IntegerField(verbose_name = 'Number of restarts')
    timeouts = models.IntegerField(verbose_name = 'Number of time-outs')
        
    def calculate_score(self):
        score=0
        if self.time_taken < 240:
            score = 240 - self.time_taken
        score = score + 100 * self.pick_green
        score = score + 75 * self.deposited_rings
        score = score - 100 * self.restarts
        score = score - 50 * self.timeouts
        #score = score - 75 * self.red_collected
        score = score - 50 * self.damage_done
        return score

    def __unicode__(self):
        return 'First Abyss round for team \'' + str(self.team) + '\''

class AbyssSecondRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'AB', 'promoted_to__exact' : 2 })

    pick_green = models.IntegerField(verbose_name = 'Number of green rings picked:')
    deposited_rings = models.IntegerField(verbose_name = 'Number of rings deposited:')
    red_collected = models.IntegerField(verbose_name = 'Number of red rings collected:')
    damage_done = models.IntegerField(verbose_name = 'Number of Damages:') 
    time_taken = models.IntegerField(verbose_name = 'Time taken')
    restarts = models.IntegerField(verbose_name = 'Number of restarts')
    timeouts = models.IntegerField(verbose_name = 'Number of time-outs')
        
    def calculate_score(self):
        score=0
        if self.time_taken < 240:
            score = 240 - self.time_taken
        score = score + 100 * self.pick_green
        score = score + 75 * self.deposoted_rings
        score = score - 100 * self.restarts
        score = score - 50 * self.timeouts
        score = score - 75 * self.red_collected
        score = score - 50 * self.damage_done
        return score
    def __unicode__(self):
        return 'Second Abyss round for team \'' + str(self.team) + '\''

class AbyssThirdRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'AB', 'promoted_to__exact' : 3 })
    
    pick_green = models.IntegerField(verbose_name = 'Number of green rings picked:')
    deposited_rings = models.IntegerField(verbose_name = 'Number of rings deposited:')
    red_collected = models.IntegerField(verbose_name = 'Number of red rings collected:')
    damage_done = models.IntegerField(verbose_name = 'Number of Damages:') 
    time_taken = models.IntegerField(verbose_name = 'Time taken')
    restarts = models.IntegerField(verbose_name = 'Number of restarts')
    timeouts = models.IntegerField(verbose_name = 'Number of time-outs')
        
    def calculate_score(self):
        score=0
        if self.time_taken < 240:
            score = 240 - self.time_taken
        score = score + 100 * self.pick_green
        score = score + 75 * self.deposoted_rings
        score = score - 100 * self.restarts
        score = score - 50 * self.timeouts
        score = score - 75 * self.red_collected
        score = score - 50 * self.damage_done
        return score
    def __unicode__(self):
        return 'Third Abyss round for team \'' + str(self.team) + '\''


class SeekerFirstRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'SE', 'promoted_to__exact' : 1 })
    correct_turn = models.IntegerField(verbose_name = 'Number of correct turns:')
    stop_end = models.IntegerField(verbose_name = 'Did bot stop correctly at end(1 for Yes 0 for No): ')
    time_taken = models.IntegerField(verbose_name='Time Taken')
    wall_hits= models.IntegerField(verbose_name='Number of times wall has been touched:')
    #correct_zone = models.IntegerField(verbose_name = 'Is bot in correct zone of final room(1 for Yes 0 for No):')
    restarts = models.IntegerField(verbose_name='Number of restarts:')
    time_outs_taken = models.IntegerField(verbose_name='Number of time-outs')

    def calculate_score(self):
        score = 0
        score = score + 50 * self.correct_turn
        score = score + 100* self.stop_end
        score = score - 50 * self.restarts
        score= score - 20 * self.wall_hits
        score = score - 20 * self.time_outs_taken
        return score

    def __unicode__(self):
        return 'First Seeker round for team \'' + str(self.team) + '\'' 


class SeekerSecondRound(_EventBase):
    
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'SE', 'promoted_to__exact' : 2 })
    correct_turn = models.IntegerField(verbose_name = 'Number of correct turns:')
    stop_end = models.IntegerField(verbose_name = 'Did bot stop correctly at end(1 for Yes 0 for No): ')
    time_taken = models.IntegerField(verbose_name='Time Taken')
    wall_hits= models.IntegerField(verbose_name='Number of times wall has been touched:')
    #correct_zone = models.IntegerField(verbose_name = 'Is bot in correct zone of final room(1 for Yes 0 for No):')
    restarts = models.IntegerField(verbose_name='Number of restarts:')
    time_outs_taken = models.IntegerField(verbose_name='Number of time-outs')

    def calculate_score(self):
        score = 0
        score = score + 50 * self.correct_turn
        score = score + 100* self.stop_end
        score = score - 50 * self.restarts
        score= score - 20 * self.wall_hits
        score = score - 20 * self.time-outs_taken
        return score 

    def __unicode__(self):
        return 'Second Seeker round for team \'' + str(self.team) + '\'' 

class SeekerThirdRound(_EventBase):

    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'SE', 'promoted_to__exact' : 2 })
    correct_turn = models.IntegerField(verbose_name = 'Number of correct turns:')
    stop_end = models.IntegerField(verbose_name = 'Did bot stop correctly at end(1 for Yes 0 for No): ')
    time_taken = models.IntegerField(verbose_name='Time Taken')
    wall_hits= models.IntegerField(verbose_name='Number of times wall has been touched:')
    correct_zone = models.IntegerField(verbose_name = 'Is bot in correct zone of final room(1 for Yes 0 for No):')
    wrong_zone = models.IntegerField(verbose_name = 'Is bot in wrong zone(1 for Yes 0 for No):')
    restarts = models.IntegerField(verbose_name='Number of restarts:')
    time_outs_taken = models.IntegerField(verbose_name='Number of time-outs')

    def calculate_score(self):
        score = 0
        score = score + 50 * self.correct_turn
        score = score + 100* self.stop_end
        score = score - 50 * self.restarts
        score = score - 20 * self.wall_hits
        score = score - 100 * self.wrong_zone
        score = score - 20 * self.time-outs_taken
        return score 

    def __unicode__(self):
        return 'Third Seeker round for team \'' + str(self.team) + '\''   


class ACROSSFirstRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'AC', 'promoted_to__exact' : 1 })
    
    lower_correct_position = models.IntegerField(verbose_name = 'Number of times lower bot positioned correctly:')
    sense_gap = models.IntegerField(verbose_name = 'Number of times upper bot sensed gap:')
    collision_blocker=models.IntegerField(verbose_name= 'Number of collisions with path blocekr:')
    collision_building = models.IntegerField(verbose_name= 'Number of collisions with buildings:')
    grids_crossed = models.IntegerField(verbose_name= 'Number of times grids crossed grazing the wall:')
    num_restarts = models.IntegerField(verbose_name = 'Number of restarts')
    num_timeouts = models.IntegerField(verbose_name = 'Number of time-outs')
   
    time_taken = models.IntegerField(verbose_name = 'Time taken')

    def calculate_score(self):
        score = 500
        score = score + 150*self.lower_correct_position
        score = score + 75*self.sense_gap
        score = score - 15*self.collision_blocker
        score = score - 15*self.collision_building
        score = score - 30*self.grids_crossed
        score = score - 40 * self. num_timeouts
        score = score - 60 * self.num_restarts
        if self.time_taken < 480:
            score= score + (480 - self.time_taken)
        return score

    def __unicode__(self):
        return 'First ACROSS round for team \'' + str(self.team) + '\''
    
class ACROSSSecondRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'AC', 'promoted_to__exact' : 2 })
    
    lower_correct_position = models.IntegerField(verbose_name = 'Number of times lower bot positioned correctly:')
    sense_gap = models.IntegerField(verbose_name = 'Number of times upper bot sensed gap:')
    collision_blocker=models.IntegerField(verbose_name= 'Number of collisions with path blocekr:')
    collision_building = models.IntegerField(verbose_name= 'Number of collisions with buildings:')
    grids_crossed = models.IntegerField(verbose_name= 'Number of times grids crossed grazing the wall:')
    num_restarts = models.IntegerField(verbose_name = 'Number of restarts')
    num_timeouts = models.IntegerField(verbose_name = 'Number of time-outs')
    time_taken = models.IntegerField(verbose_name = 'Time taken')

    def calculate_score(self):
        score = 500
        score = score + 150*self.lower_correct_position
        score = score + 75*self.sense_gap
        score = score - 15*self.collision_blocker
        score = score - 15*self.collision_building
        score = score - 30*self.grids_crossed
        score = score - 40 * self. num_timeouts
        score = score - 60 * self.num_restarts
        if self.time_taken < 600:
            score= score + (600 - self.time_taken)
        return score

def __unicode__(self):
        return 'Second ACROSS round for team \'' + str(self.team) + '\''

class ACROSSThirdRound(_EventBase):
    team = models.ForeignKey(Team, limit_choices_to = { 'event__exact' : 'AC', 'promoted_to__exact' : 3 })
    
    lower_correct_position = models.IntegerField(verbose_name = 'Number of times lower bot positioned correctly:')
    sense_gap = models.IntegerField(verbose_name = 'Number of times upper bot sensed gap:')
    collision_blocker=models.IntegerField(verbose_name= 'Number of collisions with path blocekr:')
    collision_building = models.IntegerField(verbose_name= 'Number of collisions with buildings:')
    grids_crossed = models.IntegerField(verbose_name= 'Number of times grids crossed grazing the wall:')
    num_restarts = models.IntegerField(verbose_name = 'Number of restarts')
    num_timeouts = models.IntegerField(verbose_name = 'Number of time-outs')
    time_taken = models.IntegerField(verbose_name = 'Time taken')

    def calculate_score(self):
        score = 500
        score = score + 150*self.lower_correct_position
        score = score + 75*self.sense_gap
        score = score - 15*self.collision_blocker
        score = score - 15*self.collision_building
        score = score - 30*self.grids_crossed
        score = score - 40 * self. num_timeouts
        score = score - 60 * self.num_restarts
        if self.time_taken < 600:
            score= score + (600 - self.time_taken)
        return score

    def __unicode__(self):
        return 'Third ACROSS round for team \'' + str(self.team) + '\''


def rbtx_get_model_class_by_code_and_round(code, rnd):
    """ rbtx_get_model_class_by_code_and_round ('OV', 2) will return OverhaulSecondRound etc. """
    if not rbtx_is_valid_event_code(code):
        return None
    code = upper(code)

    try:
        rnd = int(rnd)
    except ValueError:
        return None

    if code == 'LU':
        if rnd == 1:
            return LumosFirstRound
        elif rnd == 2:
            return LumosSecondRound
        elif rnd == 3:
            return LumosThirdRound
    elif code == 'OV':
        if rnd == 1:
            return OverhaulFirstRound
        elif rnd == 2:
            return OverhaulSecondRound
        elif rnd == 3:
            return OverhaulThirdRound
    elif code == 'AB':
        if rnd == 1:
            return AbyssFirstRound
        elif rnd == 2:
            return AbyssSecondRound
        elif rnd == 3:
            return AbyssThirdRound
    elif code == 'SE':
        if rnd == 1:
            return SeekerFirstRound
        elif rnd == 2:
            return SeekerSecondRound
        elif rnd == 3:
            return SeekerThirdRound
    elif code == 'AC':
        if rnd == 1:
            return ACROSSFirstRound
        elif rnd == 2:
            return ACROSSSecondRound
        elif rnd ==3:
            return ACROSSThirdRound
    return None

def rbtx_get_model_list():
    return [ LumosFirstRound, LumosSecondRound, LumosThirdRound, OverhaulFirstRound, OverhaulSecondRound, OverhaulThirdRound, AbyssFirstRound, AbyssSecondRound, AbyssThirdRound, ACROSSFirstRound, ACROSSSecondRound, ACROSSThirdRound ]

