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
        # Migration page - combined personal attitudes and network assessments
        if USE_LLM:
            persona_id = hash(str(self.participant.id_in_session)) % 5
            persona = LLMBotPersona(persona_id)
            model = os.environ.get('OLLAMA_MODEL', 'llama3.2')

            # Get LLM responses for personal migration attitudes
            responses = get_response_for_page(
                'Migration',
                ['migration_culture', 'migration_return', 'migration_limit',
                 'migration_number', 'migration_social', 'migration_border', 'migration_eco'],
                'app_migration',
                persona,
                model
            )
            migration_data = responses
        else:
            migration_data = {
                # Personal migration attitudes
                'migration_culture': random.randint(0, 7),
                'migration_return': random.randint(0, 7),
                'migration_limit': random.randint(0, 7),
                'migration_number': random.randint(0, 7),
                'migration_social': random.randint(0, 7),
                'migration_border': random.randint(0, 7),
                'migration_eco': random.randint(0, 7),
            }

        # Add migration economy network assessments (keep random)
        migration_data.update({f'migration_eco_{i}': random.randint(0, 7) for i in range(1, 51)})
        # Add migration culture network assessments (keep random)
        migration_data.update({f'migration_culture_{i}': random.randint(0, 7) for i in range(1, 51)})

        yield Submission(pages.Migration, migration_data, check_html=False)
