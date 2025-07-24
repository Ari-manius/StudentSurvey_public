from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
import json
import os

def load_questions():
    """Load questions from JSON file"""
    questions_path = os.path.join(os.path.dirname(__file__), 'questions.json')
    with open(questions_path, 'r', encoding='utf-8') as f:
        return json.load(f)

class FreshersCamp(Page):
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['FreshersCamp']['questions']
        }
    form_model = Player
    form_fields = ['fresherscamp_student', 'freshersweek_student']

class Tutorials(Page): #13
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Tutorials']['questions']
        }
    form_model = Player
    form_fields = ['tutorial', 'grade']


class Study(Page):
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Study']['questions']
        }
    form_model = Player
    form_fields = ['study_program', 'study_program_other', 'semester_of_study', 'consecutive_study_program']
 

page_sequence = [Study, FreshersCamp, Tutorials]
