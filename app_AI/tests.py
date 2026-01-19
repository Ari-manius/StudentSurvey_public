from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # AI_use page - test for new participants
        if not self.participant.is_returning_participant:
            yield pages.AI_use, dict(
                AI_use_1=random.choice([True, False]),
                AI_use_2=random.choice([True, False]),
                AI_use_3=random.choice([True, False]),
                AI_use_4=random.choice([True, False]),
                AI_use_5=random.choice([True, False]),
                AI_use_no=random.choice([True, False]),
                AI_use_other="",
                AI_tool_1=random.choice([True, False]),
                AI_tool_2=random.choice([True, False]),
                AI_tool_3=random.choice([True, False]),
                AI_tool_4=random.choice([True, False]),
                AI_tool_5=random.choice([True, False]),
                AI_tool_no=random.choice([True, False]),
                AI_tool_other="",
                AI_subscription=random.randint(0, 2),
                AI_prompt=""
            )
