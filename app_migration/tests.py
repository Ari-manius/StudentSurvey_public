from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # Migration page - combined personal attitudes and network assessments
        migration_data = {
            # Personal migration attitudes
            'migration_culture': random.randint(0, 7),
            'migration_return': random.randint(0, 7),
            'migration_limit': random.randint(0, 7),
            'migration_number': random.randint(0, 7),
            'migration_social': random.randint(0, 7),
            'migration_border': random.randint(0, 7),
            'migration_eco': random.randint(0, 7),
        }
        # Add migration economy network assessments
        migration_data.update({f'migration_eco_{i}': random.randint(0, 7) for i in range(1, 51)})
        # Add migration culture network assessments
        migration_data.update({f'migration_culture_{i}': random.randint(0, 7) for i in range(1, 51)})

        yield Submission(pages.Migration, migration_data, check_html=False)
