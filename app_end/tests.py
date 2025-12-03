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
    from llm_bot_helper import LLMBotPersona
    USE_LLM = os.environ.get('USE_LLM_BOTS', '0') == '1'
except ImportError:
    USE_LLM = False


class PlayerBot(Bot):
    def play_round(self):
        if USE_LLM:
            # Initialize persona for potential future use
            persona_id = hash(str(self.participant.id_in_session)) % 5
            persona = LLMBotPersona(persona_id)
        # NetworkNarrative page - COMMENTED OUT: Not in page_sequence
        # yield pages.NetworkNarrative, dict(
        #     network_narrative=random.choice(['No comments', 'Great survey!', 'Interesting questions', ''])
        # )

        # RandomNumber page - needs participant label + random number
        label = self.participant.label
        number = self.player.rnumber
        yield pages.RandomNumber, dict(
            rnumbercheck=f"{label}_{number}"
        )

        # FirstEndPage
        yield pages.FirstEndPage, dict(
            time_firstendpage=str(random.randint(20, 40)),
            feedback=random.choice(['', 'Thank you', 'Good survey', 'No feedback'])
        )

        # End page (final page, may not have submit button)
        yield Submission(pages.End, dict(
            time_endpage=str(random.randint(1, 5))
        ), check_html=False)
