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
    age = models.IntegerField(blank=True, label="", min=10, max=100)
    gender = models.IntegerField(blank=True, max=10, min=0, label="")

    # Secondary Education 
    postcode = models.IntegerField(blank=True, label='Postcode (PP)', min=00, max=99)
    secondary_year = models.IntegerField(blank=True, label='Year of Graduation (YYYY)', min=0, max=3000)

    # Work / Academic Family Background 
    edu_family_1gen_m = models.IntegerField(blank=True, max=9, min=0, label="")
    edu_family_1gen_f = models.IntegerField(blank=True, max=9, min=0, label="")
    edu_family_2gen_m1 = models.IntegerField(blank=True, max=9, min=0, label="")
    edu_family_2gen_f1 = models.IntegerField(blank=True, max=9, min=0, label="")
    edu_family_2gen_m2 = models.IntegerField(blank=True, max=9, min=0, label="")
    edu_family_2gen_f2 = models.IntegerField(blank=True, max=9, min=0, label="")
    # school_father = models.IntegerField(blank=True, max=6, min=0, label="")
    # school_mother = models.IntegerField(blank=True, max=6, min=0, label="")
    # work_edu_father = models.IntegerField(blank=True, max=9, min=0, label="")
    # work_edu_mother = models.IntegerField(blank=True, max=9, min=0, label="")
    # ocu_father = models.IntegerField(blank=True, max=3, min=0, label="")
    # ocu_mother = models.IntegerField(blank=True, max=3, min=0, label="")

    # Financial Situation
    financial_situation_personal_current = models.IntegerField(blank=True, label="", min=0, max=10)
    financial_situation_general_current = models.IntegerField(blank=True, label="", min=0, max=10)
    financial_situation_personal_future = models.IntegerField(blank=True, label="", min=0, max=10)
    financial_situation_general_future = models.IntegerField(blank=True, label="", min=0, max=10)
    time_work = models.IntegerField(blank=True, label="", min=0, max=10000)
    # rent = models.IntegerField(blank=True, label="", min=0, max=10000)
    # income = models.IntegerField(blank=True, label="", min=0, max=10000)

