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

class Class(Page): #13
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Class']['questions']
        }
    form_model = Player
    form_fields = ['time_class', 'tutorial', 'grade_expectation']

class MotivatedStrategies(Page): #13
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['MotivatedStrategies']['questions']
        }
    form_model = Player
    form_fields = [
        'motivation_intrinsic_goal',
        'motivation_extrinsic_goal',
        'motivation_task_value',
        'expentancy_control_learning',
        'expentancy_self_efficacy_learning',
        'affective_test_anxiety',
        'affective_academic_stress',
        'resource_time',
        'resource_effort',
        'resource_peer',
        'resource_help'
    ]

class Study(Page):
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Study']['questions']
        }
    form_model = Player
    form_fields = ['study_program', 
                    'semester_of_study', 
                    'consecutive_academic_career']
 
page_sequence = [Study, FreshersCamp, Class, MotivatedStrategies]
