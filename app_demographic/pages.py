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
    form_fields = ['age', 'gender']


class LevelFamily(Page): #3
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['LevelFamily']['questions']
        }
    form_model = Player
    form_fields = ['work_edu_father', 'work_edu_mother', 'ocu_mother', 'ocu_father', 'school_mother', 'school_father']

class Financial(Page): #3
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Financial']['questions']
        }
    form_model = Player
    form_fields = ['rent', 'income']

class Secondary(Page):
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Secondary']['questions']
        }
    form_model = Player
    form_fields = ['postcode', 'secondary_year']

page_sequence = [GenderAge, Secondary, LevelFamily, Financial]
