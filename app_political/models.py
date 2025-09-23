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
    name_in_url = 'app_political'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ### Sonntagsfrage
    sunday_poll = models.IntegerField(blank=True, max=4, min=1, label="")
    sunday_party_vote = models.IntegerField(blank=True, max=8, min=1, label="")
    sunday_not_eligible = models.IntegerField(blank=True, max=8, min=1, label="")
    noteligible_sunday_party_vote = models.IntegerField(blank=True, max=8, min=1, label="")
    reason_no_vote = models.StringField(blank=True, label="")

    lr_CDU = models.StringField(blank=True, initial="0")
    lr_CSU = models.StringField(blank=True, initial="0")
    lr_SPD = models.StringField(blank=True, initial="0")
    lr_Gruene = models.StringField(blank=True, initial="0")
    lr_FDP = models.StringField(blank=True, initial="0")
    lr_Linke = models.StringField(blank=True, initial="0")
    lr_AfD = models.StringField(blank=True, initial="0")
    lr_BSW = models.StringField(blank=True, initial="0")

     ### scalometer parties
    scalo_cdu = models.StringField(blank=True)
    scalo_csu = models.StringField(blank=True)
    scalo_spd = models.StringField(blank=True)
    scalo_gruene = models.StringField(blank=True)
    scalo_fdp = models.StringField(blank=True)
    scalo_afd = models.StringField(blank=True)
    scalo_linke = models.StringField(blank=True)
    scalo_bsw = models.StringField(blank=True)

    ### scalometer peps
    scalo_pep1 = models.StringField(blank=True, initial="0") # Scholz
    scalo_pep2 = models.StringField(blank=True, initial="0") # Harris 
    scalo_pep3 = models.StringField(blank=True, initial="0") # Lauterbach
    scalo_pep4 = models.StringField(blank=True, initial="0") # Lindner
    scalo_pep5 = models.StringField(blank=True, initial="0") # Merz
    scalo_pep6 = models.StringField(blank=True, initial="0") # Zelenski  
    scalo_pep7 = models.StringField(blank=True, initial="0") # Trump
    scalo_pep8 = models.StringField(blank=True, initial="0") # Habeck
    scalo_pep9 = models.StringField(blank=True, initial="0") # Thunberg
    scalo_pep10 = models.StringField(blank=True, initial="0") # Putin
    scalo_pep11 = models.StringField(blank=True, initial="0") # Höcke
    scalo_pep12 = models.StringField(blank=True, initial="0") # Söder
    scalo_pep13 = models.StringField(blank=True, initial="0") # Baerbock
    scalo_pep14 = models.StringField(blank=True, initial="0") # Weidel
    scalo_pep15 = models.StringField(blank=True, initial="0") # Wagenknecht
    scalo_pep16 = models.StringField(blank=True, initial="0") # Netanjahu 

    politics_question_one = models.StringField(blank=True, initial='0')
    politics_question_two = models.StringField(blank=True, initial='0')
    politics_question_three = models.StringField(blank=True, initial='0')
    politics_question_four = models.StringField(blank=True, initial='0')
    politics_question_five = models.StringField(blank=True, initial='0')
    politics_question_six = models.StringField(blank=True, initial='0')
    politics_question_seven = models.StringField(blank=True, initial='0')


    social_networks_1 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_2 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_3 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_4 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_5 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_6 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_7 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_8 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_9 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_10 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_11 = models.StringField(blank=True, label="Andere/Other:")

    participation_demonstration = models.IntegerField(blank=True, max=2, min=0, label="")
    participation_demonstration_1 = models.IntegerField(blank=True, max=2, min=0, label="")
    petition_signatory = models.IntegerField(blank=True, max=2, min=0, label="")
    petition_signatory_1 = models.IntegerField(blank=True, max=2, min=0, label = "")

    linksrechts_self = models.IntegerField(blank=True, max=11, min=1, label="")