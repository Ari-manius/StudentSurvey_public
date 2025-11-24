from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # NetworkNarrative page
        yield pages.NetworkNarrative, dict(
            network_narrative=random.choice(['No comments', 'Great survey!', 'Interesting questions', ''])
        )

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
