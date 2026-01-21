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
    name_in_url = 'app_demographic'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Personal 
    age = models.IntegerField(blank=True, label="", min=1980, max=2025)
    gender = models.IntegerField(blank=True, max=10, min=0, label="")

    # Secondary Education 
    postcode = models.IntegerField(blank=True, min=00, max=99)
    secondary_year = models.IntegerField(blank=True, min=1980, max=2025)

    # Work / Academic Family Background 
    edu_family_1gen_m = models.IntegerField(blank=True, max=11, min=0, label="")
    edu_family_1gen_f = models.IntegerField(blank=True, max=11, min=0, label="")
    edu_family_2gen_m1 = models.IntegerField(blank=True, max=11, min=0, label="")
    edu_family_2gen_f1 = models.IntegerField(blank=True, max=11, min=0, label="")
    edu_family_2gen_m2 = models.IntegerField(blank=True, max=11, min=0, label="")
    edu_family_2gen_f2 = models.IntegerField(blank=True, max=11, min=0, label="")

    # Financial Situation
    financial_situation_personal_current = models.IntegerField(blank=True, label="", min=0, max=10)
    financial_situation_general_current = models.IntegerField(blank=True, label="", min=0, max=10)
    financial_situation_personal_future = models.IntegerField(blank=True, label="", min=0, max=10)
    financial_situation_general_future = models.IntegerField(blank=True, label="", min=0, max=10)
    time_work = models.IntegerField(blank=True, label="", min=0, max=168)

    # Timestamp tracking for GenderAge page
    gender_age_page_load_time = models.StringField(blank=True)
    gender_age_page_submit_time = models.StringField(blank=True)
    gender_age_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for LevelFamily page
    level_family_page_load_time = models.StringField(blank=True)
    level_family_page_submit_time = models.StringField(blank=True)
    level_family_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for Financial page
    financial_page_load_time = models.StringField(blank=True)
    financial_page_submit_time = models.StringField(blank=True)
    financial_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for Secondary page
    secondary_page_load_time = models.StringField(blank=True)
    secondary_page_submit_time = models.StringField(blank=True)
    secondary_page_duration_seconds = models.FloatField(blank=True)

