from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # Migration page (only if not returning participant)
        if pages.Migration.is_displayed(self):
            # This page has no form fields, just displays information
            yield pages.Migration, {}
