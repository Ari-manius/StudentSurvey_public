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

class Migration(Page): #3
    def is_displayed(self):
        # Only show to new participants (not returning)
        return not self.participant.is_returning_participant

    def vars_for_template(self):
        questions_data = load_questions()
        return {
            'lang': self.participant.vars.get('language'),
            'questions': questions_data['Migration']['questions']
        }
    form_model = Player
    form_fields = []

page_sequence = [
                 Migration
                 ]
