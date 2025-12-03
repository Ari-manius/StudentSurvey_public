from otree.api import Currency as c, currency_range, Submission
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
        if USE_LLM:
            persona_id = hash(str(self.participant.id_in_session)) % 5
            persona = LLMBotPersona(persona_id)
            model = os.environ.get('OLLAMA_MODEL', 'llama3.2')
        # Participation page
        if USE_LLM:
            responses = get_response_for_page(
                'Participation',
                ['participation_demonstration', 'petition_signatory',
                 'social_networks_1', 'social_networks_2', 'social_networks_3',
                 'social_networks_4', 'social_networks_5', 'social_networks_6',
                 'social_networks_7', 'social_networks_8', 'social_networks_9',
                 'social_networks_10', 'social_networks_11', 'social_networks_12'],
                'app_political',
                persona,
                model
            )
            responses['social_networks_13'] = random.choice(['', 'Other platform'])
            yield Submission(pages.Participation, responses, check_html=False)
        else:
            yield Submission(pages.Participation, dict(
                participation_demonstration=random.randint(0, 2),
                petition_signatory=random.randint(0, 2),
                social_networks_1=random.randint(0, 2),
                social_networks_2=random.randint(0, 2),
                social_networks_3=random.randint(0, 2),
                social_networks_4=random.randint(0, 2),
                social_networks_5=random.randint(0, 2),
                social_networks_6=random.randint(0, 2),
                social_networks_7=random.randint(0, 2),
                social_networks_8=random.randint(0, 2),
                social_networks_9=random.randint(0, 2),
                social_networks_10=random.randint(0, 2),
                social_networks_11=random.randint(0, 2),
                social_networks_12=random.randint(0, 2),
                social_networks_13=random.choice(['', 'Other platform'])
            ), check_html=False)

        # LeftRightParty, ScaloParty, ScaloPerson, PoliticalQuestions, Sonntagsfrage
        # These pages use LLM if enabled, otherwise random
        if USE_LLM:
            # LLM for party ratings and political questions
            lr_responses = get_response_for_page(
                'LeftRightParty',
                ['lr_CDU', 'lr_CSU', 'lr_SPD', 'lr_Gruene', 'lr_FDP', 'lr_Linke', 'lr_AfD', 'lr_BSW'],
                'app_political',
                persona,
                model
            )
            # Convert to strings
            lr_responses = {k: str(v) for k, v in lr_responses.items()}
            yield pages.LeftRightParty, lr_responses

            scalo_responses = get_response_for_page(
                'ScaloParty',
                ['scalo_cdu', 'scalo_csu', 'scalo_spd', 'scalo_gruene', 'scalo_fdp', 'scalo_linke', 'scalo_afd', 'scalo_bsw'],
                'app_political',
                persona,
                model
            )
            scalo_responses = {k: str(v) for k, v in scalo_responses.items()}
            yield pages.ScaloParty, scalo_responses

            # ScaloPerson - keep random for now (20 people)
            scalo_peps = {f'scalo_pep{i}': str(random.randint(0, 10)) for i in range(1, 21)}
            yield pages.ScaloPerson, scalo_peps

            pol_responses = get_response_for_page(
                'PoliticalQuestions',
                ['politics_question_one', 'politics_question_two', 'politics_question_three',
                 'politics_question_four', 'politics_question_five', 'politics_question_six', 'politics_question_seven'],
                'app_political',
                persona,
                model
            )
            pol_responses = {k: str(v) for k, v in pol_responses.items()}
            yield pages.PoliticalQuestions, pol_responses

            sunday_responses = get_response_for_page(
                'Sonntagsfrage',
                ['sunday_party_vote'],
                'app_political',
                persona,
                model
            )
            yield pages.Sonntagsfrage, sunday_responses
        else:
            # Random responses (original)
            yield pages.LeftRightParty, dict(
                lr_CDU=str(random.randint(0, 11)),
                lr_CSU=str(random.randint(0, 11)),
                lr_SPD=str(random.randint(0, 11)),
                lr_Gruene=str(random.randint(0, 11)),
                lr_FDP=str(random.randint(0, 11)),
                lr_Linke=str(random.randint(0, 11)),
                lr_AfD=str(random.randint(0, 11)),
                lr_BSW=str(random.randint(0, 11))
            )

            yield pages.ScaloParty, dict(
                scalo_cdu=str(random.randint(0, 10)),
                scalo_csu=str(random.randint(0, 10)),
                scalo_spd=str(random.randint(0, 10)),
                scalo_gruene=str(random.randint(0, 10)),
                scalo_fdp=str(random.randint(0, 10)),
                scalo_linke=str(random.randint(0, 10)),
                scalo_afd=str(random.randint(0, 10)),
                scalo_bsw=str(random.randint(0, 10))
            )

            scalo_peps = {f'scalo_pep{i}': str(random.randint(0, 10)) for i in range(1, 21)}
            yield pages.ScaloPerson, scalo_peps

            yield pages.PoliticalQuestions, dict(
                politics_question_one=str(random.randint(1, 7)),
                politics_question_two=str(random.randint(1, 7)),
                politics_question_three=str(random.randint(1, 7)),
                politics_question_four=str(random.randint(1, 7)),
                politics_question_five=str(random.randint(1, 7)),
                politics_question_six=str(random.randint(1, 7)),
                politics_question_seven=str(random.randint(1, 7))
            )

            yield pages.Sonntagsfrage, dict(
                sunday_party_vote=random.randint(0, 11)
            )
