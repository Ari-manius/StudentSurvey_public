from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # Financial page
        yield pages.Financial, dict(
            financial_situation_general_current=random.randint(0, 10),
            financial_situation_personal_current=random.randint(0, 10),
            financial_situation_general_future=random.randint(0, 10),
            financial_situation_personal_future=random.randint(0, 10),
            time_work=random.randint(0, 40)
        )

        # GenderAge page (only if not returning participant)
        if pages.GenderAge.is_displayed(self):
            yield pages.GenderAge, dict(
                age=random.randint(2000, 2008),
                gender=random.randint(0, 10)
            )

        # Secondary page (only if not returning participant)
        if pages.Secondary.is_displayed(self):
            yield pages.Secondary, dict(
                postcode=random.randint(0, 99),
                secondary_year=random.randint(2010, 2022)
            )

        # LevelFamily page (only if not returning participant)
        if pages.LevelFamily.is_displayed(self):
            yield pages.LevelFamily, dict(
                edu_family_1gen_m=random.randint(0, 11),
                edu_family_1gen_f=random.randint(0, 11),
                edu_family_2gen_m1=random.randint(0, 11),
                edu_family_2gen_f1=random.randint(0, 11),
                edu_family_2gen_m2=random.randint(0, 11),
                edu_family_2gen_f2=random.randint(0, 11)
            )
