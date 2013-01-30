from eventmanager.models import *

def rbtx_find_team_by_id(team_id):
    """ Take a team ID of the form AC123 and return a Team object if possible, otherwise return None """
    if len(team_id) < 3:
        return None
    event_code = upper(team_id [:2])
    try:
        team_no = int(team_id [2:])
    except ValueError:
        return None
    if not rbtx_is_valid_event_code(event_code):
        return None
    return Team.objects.get(team_id = team_no, event = event_code)
