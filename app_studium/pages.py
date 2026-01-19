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
    def is_displayed(self):
        # Only show to new participants (not returning)
        return not self.participant.is_returning_participant

    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', 'en')
        lang_code = 0 if language == 'de' else 1
        return {
            'lang': lang_code,
            'questions': questions_data['FreshersCamp']['questions']
        }
    form_model = Player
    form_fields = ['fresherscamp_student', 'freshersweek_student',
                   'freshers_camp_page_load_time', 'freshers_camp_page_submit_time', 'freshers_camp_page_duration_seconds']

class Class(Page): #13
    def vars_for_template(self):
        questions_data = load_questions()
        # Get all players for this participant to access network app data
        all_players = self.participant.get_players()
        network_player = None
        for p in all_players:
            if hasattr(p, 'person_1'):  # Check if this is the network app player
                network_player = p
                break

        language = self.participant.vars.get('language', 'en')
        lang_code = 0 if language == 'de' else 1
        return {
            'lang': lang_code,
            'questions': questions_data['Class']['questions'],
            'network_player': network_player
        }
    form_model = Player
    form_fields = ['tutorial', 'grade', 'time_class',
                   'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10', 'grade_11',
                   'grade_12', 'grade_13', 'grade_14', 'grade_15', 'grade_16', 'grade_17', 'grade_18', 'grade_19', 'grade_20', 'grade_21',
                   'grade_22', 'grade_23', 'grade_24', 'grade_25', 'grade_26', 'grade_27', 'grade_28', 'grade_29', 'grade_30', 'grade_31',
                   'grade_32', 'grade_33', 'grade_34', 'grade_35', 'grade_36', 'grade_37', 'grade_38', 'grade_39', 'grade_40', 'grade_41',
                   'grade_42', 'grade_43', 'grade_44', 'grade_45', 'grade_46', 'grade_47', 'grade_48', 'grade_49', 'grade_50',
                   'class_page_load_time', 'class_page_submit_time', 'class_page_duration_seconds']

class MotivatedStrategies(Page): #13
    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', 'en')
        lang_code = 0 if language == 'de' else 1
        return {
            'lang': lang_code,
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
        'resource_help',
        'motivated_strategies_page_load_time',
        'motivated_strategies_page_submit_time',
        'motivated_strategies_page_duration_seconds'
    ]

class Study(Page):
    def is_displayed(self):
        # Only show to new participants (not returning)
        return not self.participant.is_returning_participant

    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', 'en')
        lang_code = 0 if language == 'de' else 1
        return {
            'lang': lang_code,
            'questions': questions_data['Study']['questions']
        }
    form_model = Player
    form_fields = ['study_program', # move over to demographics
                    'semester_of_study', # move over to demographics
                    'consecutive_academic_career',
                    'study_page_load_time',
                    'study_page_submit_time',
                    'study_page_duration_seconds']
 
page_sequence = [
                FreshersCamp,
                Study,
                Class,
                MotivatedStrategies
                ]
