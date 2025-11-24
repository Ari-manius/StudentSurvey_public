from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # Participation page
        yield Submission(pages.Participation, dict(
            participation_demonstration=random.randint(0, 2),
            petition_signatory=random.randint(0, 2),
            social_networks_1=random.randint(0, 2),
            social_networks_2=random.randint(0, 2),
            social_networks_3=random.randint(0, 2),
            social_networks_4=random.randint(0, 2),
            social_networks_5=random.randint(0, 2),
            social_networks_6=random.randint(0, 2),
            social_networks_7=random.randint(0, 2),
            social_networks_8=random.randint(0, 2),
            social_networks_9=random.randint(0, 2),
            social_networks_10=random.randint(0, 2),
            social_networks_11=random.randint(0, 2),
            social_networks_12=random.randint(0, 2),
            social_networks_13=random.choice(['', 'Other platform'])
        ), check_html=False)

        # LeftRightParty page
        yield pages.LeftRightParty, dict(
            lr_CDU=str(random.randint(0, 11)),
            lr_CSU=str(random.randint(0, 11)),
            lr_SPD=str(random.randint(0, 11)),
            lr_Gruene=str(random.randint(0, 11)),
            lr_FDP=str(random.randint(0, 11)),
            lr_Linke=str(random.randint(0, 11)),
            lr_AfD=str(random.randint(0, 11)),
            lr_BSW=str(random.randint(0, 11))
        )

        # ScaloParty page
        yield pages.ScaloParty, dict(
            scalo_cdu=str(random.randint(0, 10)),
            scalo_csu=str(random.randint(0, 10)),
            scalo_spd=str(random.randint(0, 10)),
            scalo_gruene=str(random.randint(0, 10)),
            scalo_fdp=str(random.randint(0, 10)),
            scalo_linke=str(random.randint(0, 10)),
            scalo_afd=str(random.randint(0, 10)),
            scalo_bsw=str(random.randint(0, 10))
        )

        # ScaloPerson page
        scalo_peps = {f'scalo_pep{i}': str(random.randint(0, 10)) for i in range(1, 21)}
        yield pages.ScaloPerson, scalo_peps

        # PoliticalQuestions page
        yield pages.PoliticalQuestions, dict(
            politics_question_one=str(random.randint(1, 7)),
            politics_question_two=str(random.randint(1, 7)),
            politics_question_three=str(random.randint(1, 7)),
            politics_question_four=str(random.randint(1, 7)),
            politics_question_five=str(random.randint(1, 7)),
            politics_question_six=str(random.randint(1, 7)),
            politics_question_seven=str(random.randint(1, 7))
        )

        # Sonntagsfrage page
        yield pages.Sonntagsfrage, dict(
            sunday_party_vote=random.randint(0, 11)
        )
