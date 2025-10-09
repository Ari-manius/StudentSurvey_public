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
    # Study
    semester_of_study = models.IntegerField(blank=True, max=24, min=1, label="Enter number (1-24)")
    study_program = models.IntegerField(blank=True, max=4, min=0)
    #study_program_other = models.StringField(blank=True, label="Andere/Other:")
    consecutive_academic_career = models.IntegerField(blank=True, max=4, min=0)

    # Class
    tutorial = models.IntegerField(blank=True, max=8, min=0, label="")
    grade_expectation = models.IntegerField(blank=True)
    time_class = models.IntegerField(blank=True, label="Hours per week (0-100)", min=0, max=100)

    # MSL
    motivation_intrinsic_goal = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_extrinsic_goal = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_task_value = models.IntegerField(blank=True, max=8, min=0, label="")

    expentancy_control_learning = models.IntegerField(blank=True, max=8, min=0, label="")
    expentancy_self_efficacy_learning = models.IntegerField(blank=True, max=8, min=0, label="")

    affective_test_anxiety = models.IntegerField(blank=True, max=8, min=0, label="")
    affective_academic_stress = models.IntegerField(blank=True, max=8, min=0, label="")

    resource_time = models.IntegerField(blank=True, max=8, min=0, label="")
    resource_effort = models.IntegerField(blank=True, max=8, min=0, label="")
    resource_peer = models.IntegerField(blank=True, max=8, min=0, label="")
    resource_help = models.IntegerField(blank=True, max=8, min=0, label="")

    # Social 
    fresherscamp_student = models.IntegerField(blank=True, max= 5, min=0, label="")    
    freshersweek_student = models.IntegerField(blank=True, max= 2, min=0, label="")
