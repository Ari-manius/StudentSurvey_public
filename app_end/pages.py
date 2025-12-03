from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *

class NetworkNarrative(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ["network_narrative"]

class RandomNumber(Page): #16
    def vars_for_template(self):
        label = self.participant.label
        return {'rnumber': safe_json(self.player.rnumber),
                'student_code': label,
                'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['rnumbercheck']

class FirstEndPage(Page): #14
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['time_firstendpage', 'feedback']

class End(Page): #15
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['time_endpage']

page_sequence = [RandomNumber, FirstEndPage, End]
