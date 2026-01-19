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

    migration_eco_1 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_2 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_3 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_4 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_5 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_6 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_7 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_8 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_9 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_10 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_11 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_12 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_13 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_14 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_15 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_16 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_17 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_18 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_19 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_20 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_21 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_22 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_23 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_24 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_25 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_26 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_27 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_28 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_29 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_30 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_31 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_32 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_33 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_34 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_35 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_36 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_37 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_38 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_39 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_40 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_41 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_42 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_43 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_44 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_45 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_46 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_47 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_48 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_49 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_eco_50 = models.IntegerField(blank=True, max=7, min=0, label="")

    migration_culture_1 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_2 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_3 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_4 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_5 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_6 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_7 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_8 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_9 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_10 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_11 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_12 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_13 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_14 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_15 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_16 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_17 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_18 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_19 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_20 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_21 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_22 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_23 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_24 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_25 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_26 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_27 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_28 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_29 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_30 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_31 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_32 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_33 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_34 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_35 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_36 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_37 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_38 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_39 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_40 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_41 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_42 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_43 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_44 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_45 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_46 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_47 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_48 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_49 = models.IntegerField(blank=True, max=7, min=0, label="")
    migration_culture_50 = models.IntegerField(blank=True, max=7, min=0, label="")

    # Timestamp tracking for Migration page
    migration_page_load_time = models.StringField(blank=True)
    migration_page_submit_time = models.StringField(blank=True)
    migration_page_duration_seconds = models.FloatField(blank=True)
