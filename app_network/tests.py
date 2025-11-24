from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # NetworkNamedPersons - all persons default to "x"
        person_data = {f'person_{i}': 'x' for i in range(1, 51)}
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

        # AcademicNetworkAssessment - grades for each person (0-11)
        grade_data = {f'grade_{i}': random.randint(0, 11) for i in range(1, 51)}
        yield Submission(pages.AcademicNetworkAssessment, grade_data, check_html=False)

        # LeftrightSelfAssessment
        yield pages.LeftrightSelfAssessment, dict(
            linksrechts_self=random.randint(0, 11)
        )

        # LeftrightNetworkAssessment - left-right scale for each person (0-11)
        linksrechts_data = {f'linksrechts_{i}': random.randint(0, 11) for i in range(1, 51)}
        yield Submission(pages.LeftrightNetworkAssessment, linksrechts_data, check_html=False)

        # MigrationEconomyAssessment - migration economy views for each person (0-7)
        migration_eco_data = {f'migration_eco_{i}': random.randint(0, 7) for i in range(1, 51)}
        yield Submission(pages.MigrationEconomyAssessment, migration_eco_data, check_html=False)

        # MigrationCultureAssessment - migration culture views for each person (0-7)
        migration_culture_data = {f'migration_culture_{i}': random.randint(0, 7) for i in range(1, 51)}
        yield Submission(pages.MigrationCultureAssessment, migration_culture_data, check_html=False)
