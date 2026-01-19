

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

author = ''

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'start'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    browser = models.IntegerField()
    lang = models.IntegerField()
    use_of_device = models.IntegerField(blank=True, max=3, min=1, label="")

    # Timestamp tracking for Welcome page
    start_page_load_time = models.StringField(blank=True, doc="ISO timestamp when Welcome page loads")
    start_page_submit_time = models.StringField(blank=True, doc="ISO timestamp when Welcome response submitted")
    start_page_duration_seconds = models.FloatField(blank=True, doc="Duration between page load and submission in seconds")

