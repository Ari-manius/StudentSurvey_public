from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # Welcome page
        yield pages.Welcome, dict(
            lang=random.choice([0, 1]),  # 0=English, 1=German
            time=str(random.randint(10, 30)),
            device_type=random.randint(0, 2),
            operating_system=random.randint(0, 3),
            browser=random.randint(0, 5),
            use_of_device=random.randint(1, 3)
        )
