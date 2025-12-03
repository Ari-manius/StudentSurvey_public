from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random
import os
import sys

# Try to import LLM bot helper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils', 'bot_testing'))

try:
    from llm_bot_helper import LLMBotPersona
    USE_LLM = os.environ.get('USE_LLM_BOTS', '0') == '1'
except ImportError:
    USE_LLM = False


def get_valid_codes():
    """Load valid participant codes from room file for testing"""
    code_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '_rooms', 'code_list.txt')
    try:
        with open(code_file_path, 'r') as file:
            codes = [line.strip() for line in file.readlines()]
        return codes
    except FileNotFoundError:
        return []


class PlayerBot(Bot):
    def play_round(self):
        if USE_LLM:
            # Initialize persona for consistent behavior
            persona_id = hash(str(self.participant.id_in_session)) % 5
            persona = LLMBotPersona(persona_id)
            # Network data is complex and structural, keep random for now
            # Could enhance later with LLM-driven network generation

        # NetworkNamedPersons - use actual codes from code_list.txt
        valid_codes = get_valid_codes()
        person_data = {}

        # Randomly fill some fields with valid codes, leave others as 'x'
        for i in range(1, 51):
            if random.random() < 0.3 and valid_codes:  # 30% chance to fill with a code
                # Pick a random valid code (but not the bot's own code if it has one)
                person_data[f'person_{i}'] = random.choice(valid_codes)
            else:
                person_data[f'person_{i}'] = 'x'

        yield Submission(pages.NetworkNamedPersons, person_data, check_html=False)

        # SpecialNetworks - boolean fields for each person
        special_networks_data = {}
        for i in range(1, 51):
            special_networks_data[f'friend_{i}'] = random.choice([True, False])
            special_networks_data[f'old_{i}'] = random.choice([True, False])
            special_networks_data[f'politics_{i}'] = random.choice([True, False])
            special_networks_data[f'study_{i}'] = random.choice([True, False])
            special_networks_data[f'support_{i}'] = random.choice([True, False])
        yield Submission(pages.SpecialNetworks, special_networks_data, check_html=False)

        # GroupAssessment - group sizes for each person (0-50)
        group_data = {f'group_{i}': random.randint(0, 50) for i in range(1, 51)}
        yield Submission(pages.GroupAssessment, group_data, check_html=False)

        # LeftrightAssessment - combined self and network left-right assessment
        linksrechts_data = {'linksrechts_self': random.randint(0, 11)}
        linksrechts_data.update({f'linksrechts_{i}': random.randint(0, 11) for i in range(1, 51)})
        yield Submission(pages.LeftrightAssessment, linksrechts_data, check_html=False)
