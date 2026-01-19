from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player


class WehrdienstIntro(Page):
    template_name = 'app_vignette/Intro.html'

    def vars_for_template(self):
        language = self.participant.vars.get('language', 'en')
        lang_code = 0 if language == 'de' else 1
        return {'lang': lang_code}

    form_model = Player
    form_fields = [
        'w_baseline',
        'w_affected_family',
        'w_affected_relatives',
        'w_affected_friends',
        'w_affected_acquaintances',
        'w_affected_none',
        'w_intro_page_load_time',
        'w_intro_page_submit_time',
        'w_intro_page_duration_seconds',
    ]


class WehrdienstManipulation(Page):
    template_name = 'app_vignette/Manipulation.html'

    def vars_for_template(self):
        language = self.participant.vars.get('language', 'en')
        lang_code = 0 if language == 'de' else 1
        return {'lang': lang_code}

    form_model = Player
    form_fields = ['w_opinion', 'w_justification',
                   'w_vignette_start_time', 'w_vignette_submit_time', 'w_vignette_duration_seconds']


page_sequence = [WehrdienstIntro, WehrdienstManipulation]
