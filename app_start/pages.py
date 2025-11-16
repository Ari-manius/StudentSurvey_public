from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *
import sys
import os
# Add parent directory to path to import utils module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.participant_tracking.participant_utils import is_returning_participant

class Welcome(Page): #1
    form_model = Player
    form_fields = ['lang', 
                   'time', 
                   'device_type', 
                   'operating_system', 
                   'browser', 
                   'use_of_device']
    
    def before_next_page(self):
        self.participant.vars['language'] = self.player.lang

        participant_label = self.participant.label
        self.participant.vars['participant_label'] = participant_label

        # Check if this is a returning participant
        is_returning = is_returning_participant(participant_label)
        self.participant.is_returning_participant = is_returning

page_sequence = [Welcome] 
