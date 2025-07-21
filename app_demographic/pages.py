from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class GenderAge(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['age', 'gender']

class FreshersCamp(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')} 
    form_model = Player
    form_fields = ['fresherscamp_student', 'freshersweek_student']

class Tutorials(Page): #13
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')} 
    form_model = Player
    form_fields = ['tutorial', 'grade']

class LevelFamily(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['work_edu_father', 'work_edu_mother', 'ocu_mother', 'ocu_father', 'school_mother', 'school_father']

class Financial(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['rent', 'income']

class Postcode(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['postcode']

class Study(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['study_program', 'study_program_other', 'semester_of_study', 'consecutive_study_program']

class Participation(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['participation_demonstration',
                   'participation_demonstration_1',
                   'petition_signatory',
                   'petition_signatory_1', 
                   'social_networks_1',
                   'social_networks_2',
                   'social_networks_3',
                   'social_networks_4',
                   'social_networks_5',
                   'social_networks_6',
                   'social_networks_7',
                   'social_networks_8',
                   'social_networks_9', 
                   'social_networks_10', 
                   'social_networks_11']

page_sequence = [GenderAge, Postcode, LevelFamily , Financial, Participation,  Study, FreshersCamp,Tutorials]
