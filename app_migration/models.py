from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'app_migration'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    migration_culture = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_return = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_limit = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_number = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_social = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_border = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco = models.IntegerField(blank=True, max=7, min=0, label="")
