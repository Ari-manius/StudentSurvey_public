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

    return data

class Migration(Page):
    form_model = Player
    form_fields = ['migration_culture', 'migration_return', 'migration_limit', 'migration_number',
                   'migration_social', 'migration_border', 'migration_eco',
                   'migration_eco_1', 'migration_eco_2', 'migration_eco_3', 'migration_eco_4', 'migration_eco_5', 'migration_eco_6', 'migration_eco_7', 'migration_eco_8', 'migration_eco_9', 'migration_eco_10', 'migration_eco_11',
                   'migration_eco_12', 'migration_eco_13', 'migration_eco_14', 'migration_eco_15', 'migration_eco_16', 'migration_eco_17', 'migration_eco_18', 'migration_eco_19', 'migration_eco_20', 'migration_eco_21',
                   'migration_eco_22', 'migration_eco_23', 'migration_eco_24', 'migration_eco_25', 'migration_eco_26', 'migration_eco_27', 'migration_eco_28', 'migration_eco_29', 'migration_eco_30', 'migration_eco_31',
                   'migration_eco_32', 'migration_eco_33', 'migration_eco_34', 'migration_eco_35', 'migration_eco_36', 'migration_eco_37', 'migration_eco_38', 'migration_eco_39', 'migration_eco_40', 'migration_eco_41',
                   'migration_eco_42', 'migration_eco_43', 'migration_eco_44', 'migration_eco_45', 'migration_eco_46', 'migration_eco_47', 'migration_eco_48', 'migration_eco_49', 'migration_eco_50',
                   'migration_culture_1', 'migration_culture_2', 'migration_culture_3', 'migration_culture_4', 'migration_culture_5', 'migration_culture_6', 'migration_culture_7', 'migration_culture_8', 'migration_culture_9', 'migration_culture_10', 'migration_culture_11',
                   'migration_culture_12', 'migration_culture_13', 'migration_culture_14', 'migration_culture_15', 'migration_culture_16', 'migration_culture_17', 'migration_culture_18', 'migration_culture_19', 'migration_culture_20', 'migration_culture_21',
                   'migration_culture_22', 'migration_culture_23', 'migration_culture_24', 'migration_culture_25', 'migration_culture_26', 'migration_culture_27', 'migration_culture_28', 'migration_culture_29', 'migration_culture_30', 'migration_culture_31',
                   'migration_culture_32', 'migration_culture_33', 'migration_culture_34', 'migration_culture_35', 'migration_culture_36', 'migration_culture_37', 'migration_culture_38', 'migration_culture_39', 'migration_culture_40', 'migration_culture_41',
                   'migration_culture_42', 'migration_culture_43', 'migration_culture_44', 'migration_culture_45', 'migration_culture_46', 'migration_culture_47', 'migration_culture_48', 'migration_culture_49', 'migration_culture_50',
                   'migration_page_load_time', 'migration_page_submit_time', 'migration_page_duration_seconds']

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
            'questions': questions_data['Migration']['questions'],
            'network_player': network_player
        }

page_sequence = [Migration]
