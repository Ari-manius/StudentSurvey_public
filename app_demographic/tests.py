from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
import sys
import os

# Try to import LLM bot helper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils', 'bot_testing'))

try:
    from llm_bot_helper import LLMBotPersona, get_response_for_page
    USE_LLM = os.environ.get('USE_LLM_BOTS', '0') == '1'
except ImportError:
    USE_LLM = False


class PlayerBot(Bot):
    def play_round(self):
        # Check if we should use LLM responses
        if USE_LLM:
            # Initialize LLM persona
            persona_id = hash(str(self.participant.id_in_session)) % 5
            persona = LLMBotPersona(persona_id)
            model = os.environ.get('OLLAMA_MODEL', 'llama3.2')

            # Financial page with LLM
            responses = get_response_for_page(
                page_name='Financial',
                fields=['financial_situation_general_current',
                       'financial_situation_personal_current',
                       'financial_situation_general_future',
                       'financial_situation_personal_future',
                       'time_work'],
                app_name='app_demographic',
                persona=persona,
                model=model,
                lang='english'
            )
            yield pages.Financial, responses

            # GenderAge page with LLM
            if pages.GenderAge.is_displayed(self):
                responses = get_response_for_page(
                    page_name='GenderAge',
                    fields=['age', 'gender'],
                    app_name='app_demographic',
                    persona=persona,
                    model=model,
                    lang='english'
                )
                yield pages.GenderAge, responses

            # Secondary page with LLM
            if pages.Secondary.is_displayed(self):
                responses = get_response_for_page(
                    page_name='Secondary',
                    fields=['postcode', 'secondary_year'],
                    app_name='app_demographic',
                    persona=persona,
                    model=model,
                    lang='english'
                )
                yield pages.Secondary, responses

            # LevelFamily page with LLM
            if pages.LevelFamily.is_displayed(self):
                responses = get_response_for_page(
                    page_name='LevelFamily',
                    fields=['edu_family_1gen_m', 'edu_family_1gen_f',
                           'edu_family_2gen_m1', 'edu_family_2gen_f1',
                           'edu_family_2gen_m2', 'edu_family_2gen_f2'],
                    app_name='app_demographic',
                    persona=persona,
                    model=model,
                    lang='english'
                )
                yield pages.LevelFamily, responses

            return  # Exit after LLM responses

        # Original random-based responses (fallback)
        # Financial page
        yield pages.Financial, dict(
            financial_situation_general_current=random.randint(0, 10),
            financial_situation_personal_current=random.randint(0, 10),
            financial_situation_general_future=random.randint(0, 10),
            financial_situation_personal_future=random.randint(0, 10),
            time_work=random.randint(0, 40)
        )

        # GenderAge page (only if not returning participant)
        if pages.GenderAge.is_displayed(self):
            yield pages.GenderAge, dict(
                age=random.randint(2000, 2008),
                gender=random.randint(0, 10)
            )

        # Secondary page (only if not returning participant)
        if pages.Secondary.is_displayed(self):
            yield pages.Secondary, dict(
                postcode=random.randint(0, 99),
                secondary_year=random.randint(2010, 2022)
            )

        # LevelFamily page (only if not returning participant)
        if pages.LevelFamily.is_displayed(self):
            yield pages.LevelFamily, dict(
                edu_family_1gen_m=random.randint(0, 11),
                edu_family_1gen_f=random.randint(0, 11),
                edu_family_2gen_m1=random.randint(0, 11),
                edu_family_2gen_f1=random.randint(0, 11),
                edu_family_2gen_m2=random.randint(0, 11),
                edu_family_2gen_f2=random.randint(0, 11)
            )
