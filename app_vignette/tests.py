from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # WehrdienstIntro page
        yield pages.WehrdienstIntro, dict(
            w_baseline=random.randint(0, 7),
            w_affected_family=random.choice([True, False]),
            w_affected_relatives=random.choice([True, False]),
            w_affected_friends=random.choice([True, False]),
            w_affected_acquaintances=random.choice([True, False]),
            w_affected_none=random.choice([True, False])
        )

        # WehrdienstManipulation page
        yield pages.WehrdienstManipulation, dict(
            w_opinion=random.randint(0, 7),
            w_justification=""
        )
