from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # FreshersCamp page (only if not returning participant)
        if pages.FreshersCamp.is_displayed(self):
            yield pages.FreshersCamp, dict(
                fresherscamp_student=random.randint(0, 5),
                freshersweek_student=random.randint(0, 2)
            )

        # Study page (only if not returning participant)
        if pages.Study.is_displayed(self):
            yield pages.Study, dict(
                study_program=random.randint(0, 4),
                semester_of_study=random.randint(1, 10),
                consecutive_academic_career=random.randint(0, 4)
            )

        # Class page
        yield pages.Class, dict(
            time_class=random.randint(0, 20),
            tutorial=random.randint(0, 8),
            grade=random.choice(['1.0', '1.3', '1.7', '2.0', '2.3', '2.7', '3.0', '3.3', '3.7', '4.0', '5.0'])
        )

        # MotivatedStrategies page
        yield pages.MotivatedStrategies, dict(
            motivation_intrinsic_goal_1=random.randint(0, 8),
            motivation_extrinsic_goal_1=random.randint(0, 8),
            motivation_intrinsic_goal_2=random.randint(0, 8),
            motivation_extrinsic_goal_2=random.randint(0, 8),
            motivation_intrinsic_goal_3=random.randint(0, 8),
            motivation_extrinsic_goal_3=random.randint(0, 8),
            motivation_extrinsic_goal_4=random.randint(0, 8),
            affective_academic_stress=random.randint(0, 8),
            resource_time=random.randint(0, 8),
            resource_peer=random.randint(0, 8),
            resource_help=random.randint(0, 8)
        )
