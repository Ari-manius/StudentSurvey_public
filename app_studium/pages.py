from otree.api import Currency as c, currency_range
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
    form_fields = ['time_class', 'tutorial', 'grade']

class MotivatedStrategies(Page): #13
    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['MotivatedStrategies']['questions']
        }
    form_model = Player
    form_fields = [
        'motivation_intrinsic_goal_1',
        'motivation_extrinsic_goal_1',
        'motivation_intrinsic_goal_2',
        'motivation_extrinsic_goal_2',
        'motivation_intrinsic_goal_3',
        'motivation_extrinsic_goal_3',
        'motivation_extrinsic_goal_4',
        'affective_academic_stress',
        'resource_time',
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
 
page_sequence = [FreshersCamp, Study, Class, MotivatedStrategies]
