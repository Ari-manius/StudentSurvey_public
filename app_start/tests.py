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
            # For app_start, we'll use simple random since it's mostly technical
            # (language, device type, etc.) - not really suitable for LLM
            pass

        # app_start uses random (technical device/browser info, not suitable for LLM)
        yield pages.Welcome, dict(
            lang=random.choice([0, 1]),  # 0=English, 1=German
            time=str(random.randint(10, 30)),
            device_type=random.randint(0, 2),
            operating_system=random.randint(0, 3),
            browser=random.randint(0, 5),
            use_of_device=random.randint(1, 3)
        )
