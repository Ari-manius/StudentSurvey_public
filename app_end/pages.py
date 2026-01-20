from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *

class NetworkNarrative(Page): #8
    def vars_for_template(self):
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {'lang': lang_code}
    form_model = Player
    form_fields = ["network_narrative"]

class RandomNumber(Page): #16
    def vars_for_template(self):
        label = self.participant.label
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {'rnumber': safe_json(self.player.rnumber),
                'student_code': label,
                'lang': lang_code}
    form_model = Player
    form_fields = [
        'rnumbercheck',
        'rnumber_page_load_time',
        'rnumber_page_submit_time',
        'rnumber_page_duration_seconds'
    ]

class FirstEndPage(Page): #14
    def vars_for_template(self):
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {'lang': lang_code}
    form_model = Player
    form_fields = [
        'feedback',
        'firstend_page_load_time',
        'firstend_page_submit_time',
        'firstend_page_duration_seconds'
    ]

class End(Page): #15
    def vars_for_template(self):
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {'lang': lang_code}
    form_model = Player
    form_fields = [
        'end_page_load_time',
        'end_page_submit_time',
        'end_page_duration_seconds'
    ]

page_sequence = [RandomNumber, FirstEndPage, End]
