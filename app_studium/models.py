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
    name_in_url = 'app_studium'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Study
    semester_of_study = models.IntegerField(blank=True, max=24, min=1, label="")
    study_program = models.IntegerField(blank=True, max=4, min=0)
    consecutive_academic_career = models.IntegerField(blank=True, max=4, min=0)

    # Class
    tutorial = models.IntegerField(blank=True, max=8, min=0, label="")
    grade = models.StringField(blank=True)
    time_class = models.IntegerField(blank=True, label="", min=0, max=168, initial=0)

    # MSL
    motivation_intrinsic_goal_1 = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_intrinsic_goal_2 = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_intrinsic_goal_3 = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_extrinsic_goal_1 = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_extrinsic_goal_2 = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_extrinsic_goal_3 = models.IntegerField(blank=True, max=8, min=0, label="")
    motivation_extrinsic_goal_4 = models.IntegerField(blank=True, max=8, min=0, label="")
    affective_academic_stress = models.IntegerField(blank=True, max=8, min=0, label="")
    resource_time = models.IntegerField(blank=True, max=8, min=0, label="")
    resource_peer = models.IntegerField(blank=True, max=8, min=0, label="")
    resource_help = models.IntegerField(blank=True, max=8, min=0, label="")

    # Social
    fresherscamp_student = models.IntegerField(blank=True, max= 5, min=0, label="")
    freshersweek_student = models.IntegerField(blank=True, max= 2, min=0, label="")

    # Network Grade Assessment
    grade_1 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_2 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_3 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_4 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_5 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_6 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_7 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_8 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_9 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_10 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_11 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_12 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_13 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_14 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_15 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_16 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_17 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_18 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_19 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_20 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_21 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_22 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_23 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_24 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_25 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_26 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_27 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_28 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_29 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_30 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_31 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_32 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_33 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_34 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_35 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_36 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_37 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_38 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_39 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_40 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_41 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_42 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_43 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_44 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_45 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_46 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_47 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_48 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_49 = models.IntegerField(blank=True, max=11, min=0, label="")
    grade_50 = models.IntegerField(blank=True, max=11, min=0, label="")

    # Time tracking fields
    time_tutorial_expected_grade = models.StringField(initial="-999")
    time_postcode = models.StringField(initial="-999")
    time_fresherscamp = models.StringField(initial="-999")
