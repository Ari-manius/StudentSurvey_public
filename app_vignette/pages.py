from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player


class HarassmentVignette(Page):
    #def vars_for_template(self):
     #   return {'lang': self.participant.vars.get('language')}
    #form_model = Player
   # form_fields = ['harrassment']
        pass


class Manipulation(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['harassment']

class Results(Page):
    pass
 

page_sequence = [Manipulation]
