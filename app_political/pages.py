from ._builtin import Page
from .models import Player
import random
import os
import json

def load_questions():
    """Load questions from JSON file"""
    questions_path = os.path.join(os.path.dirname(__file__), 'questions.json')
    with open(questions_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # # Shuffle questions within each category
    # for category in data.values():
    #     if 'questions' in category and isinstance(category['questions'], list):
    #         random.shuffle(category['questions'])
    
    return data

class Sonntagsfrage(Page): #5
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['Sonntagsfrage']['questions']
        }
    form_model = Player
    form_fields = ['sunday_party_vote', 'sonntagsfrage_page_load_time', 'sonntagsfrage_page_submit_time', 'sonntagsfrage_page_duration_seconds']

class kleineSonntagsfrage(Page): # Für Landtagswahl
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['kleineSonntagsfrage']['questions']
        }
    form_model = Player
    form_fields = ['small_sunday_party_vote', 'kleine_sonntagsfrage_page_load_time', 'kleine_sonntagsfrage_page_submit_time', 'kleine_sonntagsfrage_page_duration_seconds']

class ScaloParty(Page): #6
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['ScaloParty']['questions']
        }
    form_model = Player
    form_fields = ['scalo_cdu', 'scalo_csu', 'scalo_spd', 'scalo_gruene', 'scalo_fdp', 'scalo_linke', 'scalo_afd', 'scalo_bsw',
                   'scalo_party_page_load_time', 'scalo_party_page_submit_time', 'scalo_party_page_duration_seconds']

class ScaloPerson(Page): #7
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['ScaloPerson']['questions']
        }
    form_model = Player
    form_fields = ['scalo_pep1', 'scalo_pep2', 'scalo_pep3', 'scalo_pep4', 'scalo_pep5', 'scalo_pep6', 'scalo_pep7', 'scalo_pep8',
                   'scalo_pep9', 'scalo_pep10', 'scalo_pep11', 'scalo_pep12', 'scalo_pep13', 'scalo_pep14', 'scalo_pep15', 'scalo_pep16', 'scalo_pep17', 'scalo_pep18', 'scalo_pep19', 'scalo_pep20', 'scalo_pep21','scalo_pep22','scalo_pep23','scalo_pep24','scalo_pep25','scalo_pep26',
                   'scalo_person_page_load_time', 'scalo_person_page_submit_time', 'scalo_person_page_duration_seconds']

class LeftRightParty(Page): #9
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['LeftRightParty']['questions']
        }
    form_model = Player
    form_fields = ['lr_CDU', 'lr_CSU', 'lr_SPD', 'lr_Gruene', 'lr_FDP', 'lr_Linke', 'lr_AfD', 'lr_BSW',
                   'leftright_party_page_load_time', 'leftright_party_page_submit_time', 'leftright_party_page_duration_seconds']

class PoliticalQuestions(Page): #10
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['PoliticalQuestions']['questions']
        }
    form_model = Player
    form_fields = ['politics_question_one', 'politics_question_two', 'politics_question_three', 'politics_question_four',
                   'politics_question_five', 'politics_question_six', 'politics_question_seven',
                   'political_questions_page_load_time', 'political_questions_page_submit_time', 'political_questions_page_duration_seconds']

class Participation(Page):
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def is_displayed(self):
        # Only show to new participants (not returning)
        return not self.participant.is_returning_participant

    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
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
                   'social_networks_11',
                   'social_networks_12',
                   'social_networks_13',
                   'participation_page_load_time',
                   'participation_page_submit_time',
                   'participation_page_duration_seconds']


page_sequence = [Participation, LeftRightParty, ScaloParty, ScaloPerson, PoliticalQuestions, Sonntagsfrage, kleineSonntagsfrage]
