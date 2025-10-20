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
    sunday_party_vote = models.IntegerField(blank=True, max=11, min=0, label="")

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
    scalo_pep1 = models.StringField(blank=True, initial="0") #Boris Pistorius 
    scalo_pep2 = models.StringField(blank=True, initial="0") #Bärbel Bas 
    scalo_pep3 = models.StringField(blank=True, initial="0") #Robert Habeck
    scalo_pep4 = models.StringField(blank=True, initial="0") #Franziska Brantner 
    scalo_pep5 = models.StringField(blank=True, initial="0") #Alice Weidel
    scalo_pep6 = models.StringField(blank=True, initial="0") #Janine Wissler
    scalo_pep7 = models.StringField(blank=True, initial="0") #Jens Spahn 
    scalo_pep8 = models.StringField(blank=True, initial="0") #Markus Söder
    scalo_pep9 = models.StringField(blank=True, initial="0") #Dorothee Bär 
    scalo_pep10 = models.StringField(blank=True, initial="0") #Lars Klingbeil
    scalo_pep11 = models.StringField(blank=True, initial="0") #Tino Chrupalla 
    scalo_pep12 = models.StringField(blank=True, initial="0") #Ines Schwerdtner 
    scalo_pep13 = models.StringField(blank=True, initial="0") #Friedrich Merz
    
    scalo_pep14 = models.StringField(blank=True, initial="0") #Vladimir Putinb
    scalo_pep15 = models.StringField(blank=True, initial="0") #Donald Trump
    scalo_pep16 = models.StringField(blank=True, initial="0") #Genocidal Isreally Prime Minister
    scalo_pep17 = models.StringField(blank=True, initial="0") #Emmanuel Macron 
    scalo_pep18 = models.StringField(blank=True, initial="0") #Giorgia Meloni
    scalo_pep19 = models.StringField(blank=True, initial="0") #Keir Starmer 

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
    social_networks_11 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_12 = models.IntegerField(blank=True, max=2, min=0, label="")
    social_networks_13 = models.StringField(blank=True, label="Andere/Other:")

    participation_demonstration = models.IntegerField(blank=True, max=2, min=0, label="")
    petition_signatory = models.IntegerField(blank=True, max=2, min=0, label="")