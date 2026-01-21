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
    time_class = models.IntegerField(blank=True, label="", min=0, max=168)

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
    grade_1 = models.StringField(blank=True, label="")
    grade_2 = models.StringField(blank=True, label="")
    grade_3 = models.StringField(blank=True, label="")
    grade_4 = models.StringField(blank=True, label="")
    grade_5 = models.StringField(blank=True, label="")
    grade_6 = models.StringField(blank=True, label="")
    grade_7 = models.StringField(blank=True, label="")
    grade_8 = models.StringField(blank=True, label="")
    grade_9 = models.StringField(blank=True, label="")
    grade_10 = models.StringField(blank=True, label="")
    grade_11 = models.StringField(blank=True, label="")
    grade_12 = models.StringField(blank=True, label="")
    grade_13 = models.StringField(blank=True, label="")
    grade_14 = models.StringField(blank=True, label="")
    grade_15 = models.StringField(blank=True, label="")
    grade_16 = models.StringField(blank=True, label="")
    grade_17 = models.StringField(blank=True, label="")
    grade_18 = models.StringField(blank=True, label="")
    grade_19 = models.StringField(blank=True, label="")
    grade_20 = models.StringField(blank=True, label="")
    grade_21 = models.StringField(blank=True, label="")
    grade_22 = models.StringField(blank=True, label="")
    grade_23 = models.StringField(blank=True, label="")
    grade_24 = models.StringField(blank=True, label="")
    grade_25 = models.StringField(blank=True, label="")
    grade_26 = models.StringField(blank=True, label="")
    grade_27 = models.StringField(blank=True, label="")
    grade_28 = models.StringField(blank=True, label="")
    grade_29 = models.StringField(blank=True, label="")
    grade_30 = models.StringField(blank=True, label="")
    grade_31 = models.StringField(blank=True, label="")
    grade_32 = models.StringField(blank=True, label="")
    grade_33 = models.StringField(blank=True, label="")
    grade_34 = models.StringField(blank=True, label="")
    grade_35 = models.StringField(blank=True, label="")
    grade_36 = models.StringField(blank=True, label="")
    grade_37 = models.StringField(blank=True, label="")
    grade_38 = models.StringField(blank=True, label="")
    grade_39 = models.StringField(blank=True, label="")
    grade_40 = models.StringField(blank=True, label="")
    grade_41 = models.StringField(blank=True, label="")
    grade_42 = models.StringField(blank=True, label="")
    grade_43 = models.StringField(blank=True, label="")
    grade_44 = models.StringField(blank=True, label="")
    grade_45 = models.StringField(blank=True, label="")
    grade_46 = models.StringField(blank=True, label="")
    grade_47 = models.StringField(blank=True, label="")
    grade_48 = models.StringField(blank=True, label="")
    grade_49 = models.StringField(blank=True, label="")
    grade_50 = models.StringField(blank=True, label="")

    # Timestamp tracking for FreshersCamp page
    freshers_camp_page_load_time = models.StringField(blank=True)
    freshers_camp_page_submit_time = models.StringField(blank=True)
    freshers_camp_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for Class page
    class_page_load_time = models.StringField(blank=True)
    class_page_submit_time = models.StringField(blank=True)
    class_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for MotivatedStrategies page
    motivated_strategies_page_load_time = models.StringField(blank=True)
    motivated_strategies_page_submit_time = models.StringField(blank=True)
    motivated_strategies_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for Study page
    study_page_load_time = models.StringField(blank=True)
    study_page_submit_time = models.StringField(blank=True)
    study_page_duration_seconds = models.FloatField(blank=True)
