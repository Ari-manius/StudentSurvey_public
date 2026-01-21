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

class AI_use(Page):
    # def is_displayed(self):
    #     # Only show to new participants (not returning)
    #     return not self.participant.is_returning_participant

    def vars_for_template(self):
        questions_data = load_questions()
        language = self.participant.vars.get('language', '1')
        lang_code = int(language)
        return {
            'lang': lang_code,
            'questions': questions_data['GenderAge']['questions']
        }

    form_model = Player
    form_fields = ['AI_use_1',
                   'AI_use_2',
                   'AI_use_3',
                   'AI_use_4',
                   'AI_use_5',
                   'AI_use_no',
                   'AI_use_other',
                   'AI_tool_1',
                   'AI_tool_2',
                   'AI_tool_3',
                   'AI_tool_4',
                   'AI_tool_5',
                   'AI_tool_no',
                   'AI_tool_other',
                   'AI_subscription',
                   'AI_prompt',
                   'AI_use_other',
                   'ai_page_load_time',
                   'ai_page_submit_time',
                   'ai_page_duration_seconds']


page_sequence = [
                 AI_use
                 ]
