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
import random

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'app_studium'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tutorial = models.IntegerField(blank=True, max=8, min=0, label="")
    grade = models.StringField(blank=True, label="")

    fresherscamp_student = models.IntegerField(blank=True, max= 5, min=0, label="")
    freshersweek_student = models.IntegerField(blank=True, max= 2, min=0, label="")

    semester_of_study = models.IntegerField(blank=True, max=24, min=1, label="")
    consecutive_study_program = models.IntegerField(blank=True, max=4, min=0, label="")
    study_program = models.IntegerField(blank=True, max=4, min=0, label="")
    study_program_other = models.StringField(blank=True, label="Andere/Other:")