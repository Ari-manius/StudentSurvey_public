from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player
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

class GenderAge(Page): #3
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
            'questions': questions_data['GenderAge']['questions']
        }
    form_model = Player
    form_fields = ['age',
                    'gender',
                    'gender_age_page_load_time',
                    'gender_age_page_submit_time',
                    'gender_age_page_duration_seconds']


class LevelFamily(Page): #3
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
            'questions': questions_data['LevelFamily']['questions']
        }
    form_model = Player
    form_fields = ['edu_family_1gen_m',
                    'edu_family_1gen_f',
                    'edu_family_2gen_m1',
                    'edu_family_2gen_f1',
                    'edu_family_2gen_m2',
                    'edu_family_2gen_f2',
                    'level_family_page_load_time',
                    'level_family_page_submit_time',
                    'level_family_page_duration_seconds']

class Financial(Page):
    allow_back_button = True
    preserve_unsubmitted_inputs = True
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['Financial']['questions']
        }

    form_model = Player
    form_fields = ["financial_situation_general_current",
                    "financial_situation_personal_current",
                    "financial_situation_general_future",
                    "financial_situation_personal_future",
                    "time_work",
                    "financial_page_load_time",
                    "financial_page_submit_time",
                    "financial_page_duration_seconds"]

class Secondary(Page):
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
            'questions': questions_data['Secondary']['questions']
        }

    form_model = Player
    form_fields = ['postcode',
                    'secondary_year',
                    'secondary_page_load_time',
                    'secondary_page_submit_time',
                    'secondary_page_duration_seconds']

page_sequence = [
                 Financial,
                 GenderAge,
                 Secondary,
                 LevelFamily
                 ]
