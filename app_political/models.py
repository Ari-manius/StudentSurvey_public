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
    name_in_url = 'political_app'
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

    lr_CDU = models.StringField(blank=True, initial=-999)
    lr_CSU = models.StringField(blank=True, initial=-999)
    lr_SPD = models.StringField(blank=True, initial=-999)
    lr_Gruene = models.StringField(blank=True, initial=-999)
    lr_FDP = models.StringField(blank=True, initial=-999)
    lr_Linke = models.StringField(blank=True, initial=-999)
    lr_AfD = models.StringField(blank=True, initial=-999)
    lr_BSW = models.StringField(blank=True, initial=-999)

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
    scalo_pep1 = models.StringField(blank=True, initial=-999) # Scholz
    scalo_pep2 = models.StringField(blank=True, initial=-999) # Harris 
    scalo_pep3 = models.StringField(blank=True, initial=-999) # Lauterbach
    scalo_pep4 = models.StringField(blank=True, initial=-999) # Lindner
    scalo_pep5 = models.StringField(blank=True, initial=-999) # Merz
    scalo_pep6 = models.StringField(blank=True, initial=-999) # Zelenski  
    scalo_pep7 = models.StringField(blank=True, initial=-999) # Trump
    scalo_pep8 = models.StringField(blank=True, initial=-999) # Habeck
    scalo_pep9 = models.StringField(blank=True, initial=-999) # Thunberg
    scalo_pep10 = models.StringField(blank=True, initial=-999) # Putin
    scalo_pep11 = models.StringField(blank=True, initial=-999) # Höcke
    scalo_pep12 = models.StringField(blank=True, initial=-999) # Söder
    scalo_pep13 = models.StringField(blank=True, initial=-999) # Baerbock
    scalo_pep14 = models.StringField(blank=True, initial=-999) # Weidel
    scalo_pep15 = models.StringField(blank=True, initial=-999) # Wagenknecht
    scalo_pep16 = models.StringField(blank=True, initial=-999) # Netanjahu 

    politics_question_one = models.StringField(blank=True, initial='-999')
    politics_question_two = models.StringField(blank=True, initial='-999')
    politics_question_three = models.StringField(blank=True, initial='-999')
    politics_question_four = models.StringField(blank=True, initial='-999')
    politics_question_five = models.StringField(blank=True, initial='-999')
    politics_question_six = models.StringField(blank=True, initial='-999')
    politics_question_seven = models.StringField(blank=True, initial='-999')
    



    #time_sundayquestion=models.StringField(initial="-999")
    #time_scaloparty = models.StringField(initial="-999")
    #time_scaloperson = models.StringField(initial="-999")
    #time_leftright = models.StringField(initial="-999")
    #time_pid = models.StringField(initial="-999")
    #time_political_qs = models.StringField(initial="-999")