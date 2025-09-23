from ._builtin import Page
from .models import Player
import json
import os

def load_questions():
    """Load questions from JSON file"""
    questions_path = os.path.join(os.path.dirname(__file__), 'questions.json')
    with open(questions_path, 'r', encoding='utf-8') as f:
        return json.load(f)

class LeftrightSelfAssessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['linksrechts_self']

class Sonntagsfrage(Page): #5
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Sonntagsfrage']['questions']
        }
    form_model = Player
    form_fields = ['sunday_poll', 'sunday_party_vote', 'sunday_not_eligible', 'noteligible_sunday_party_vote', 'reason_no_vote']

class ScaloParty(Page): #6
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['ScaloParty']['questions']
        }
    form_model = Player
    form_fields = ['scalo_cdu', 'scalo_csu', 'scalo_spd', 'scalo_gruene', 'scalo_fdp', 'scalo_linke', 'scalo_afd', 'scalo_bsw']

class ScaloPerson(Page): #7
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['ScaloPerson']['questions']
        }
    form_model = Player
    form_fields = ['scalo_pep1', 'scalo_pep2', 'scalo_pep3', 'scalo_pep4', 'scalo_pep5', 'scalo_pep6', 'scalo_pep7', 'scalo_pep8',
                   'scalo_pep9', 'scalo_pep10', 'scalo_pep11', 'scalo_pep12', 'scalo_pep13', 'scalo_pep14', 'scalo_pep15', 'scalo_pep16']

class LeftRightParty(Page): #9
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['LeftRightParty']['questions']
        }
    form_model = Player
    form_fields = ['lr_CDU', 'lr_CSU', 'lr_SPD', 'lr_Gruene', 'lr_FDP', 'lr_Linke', 'lr_AfD', 'lr_BSW']

class PoliticalQuestions(Page): #10
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['PoliticalQuestions']['questions']
        }
    form_model = Player
    form_fields = ['politics_question_one', 'politics_question_two', 'politics_question_three', 'politics_question_four',
                   'politics_question_five', 'politics_question_six', 'politics_question_seven']

class Participation(Page):
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Participation']['questions']
        }
    form_model = Player
    form_fields = ['participation_demonstration',
                   'petition_signatory',
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


page_sequence = [LeftrightSelfAssessment, Participation, LeftRightParty, ScaloParty, ScaloPerson, PoliticalQuestions, Sonntagsfrage]
