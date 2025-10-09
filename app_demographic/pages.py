from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player
import json
import os

def load_questions():
    """Load questions from JSON file"""
    questions_path = os.path.join(os.path.dirname(__file__), 'questions.json')
    with open(questions_path, 'r', encoding='utf-8') as f:
        return json.load(f)

class GenderAge(Page): #3
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['GenderAge']['questions']
        }
    form_model = Player
    form_fields = ['age', 
                    'gender']


class LevelFamily(Page): #3
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['LevelFamily']['questions']
        }
    form_model = Player
    form_fields = ['edu_family_1gen_m',
                    'edu_family_1gen_f',
                    'edu_family_2gen_m1',
                    'edu_family_2gen_f1',
                    'edu_family_2gen_m2',
                    'edu_family_2gen_f2',
                   ]

class Financial(Page): 
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Financial']['questions']
        }
    form_model = Player
    form_fields = ["financial_situation_general_current",
                    "financial_situation_personal_current", 
                    "financial_situation_general_future",
                    "financial_situation_personal_future",
                    "time_work",
                    ]

class Secondary(Page):
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Secondary']['questions']
        }
    form_model = Player
    form_fields = ['postcode', 
                    'secondary_year']

page_sequence = [Financial, GenderAge, Secondary, LevelFamily]
