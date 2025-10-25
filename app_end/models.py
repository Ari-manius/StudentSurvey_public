import random
#from . import constants

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
from app_end.templates.app_end.random_number import random_number
from app_end.templates.app_end.random_number import n_random_numbers, random_number

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'app_end'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():

            p.rnumber = random_number(100000, 999999)  # for the random number check

            random_numbers_vl = n_random_numbers(1, 3, 2)
            p.randomnumber_vl_1 = random_numbers_vl[0]
            p.randomnumber_vl_2 = random_numbers_vl[1]
            random_numbers_tut = n_random_numbers(1, 3, 2)
            p.randomnumber_tut_1 = random_numbers_tut[0]
            p.randomnumber_tut_2 = random_numbers_tut[1]
            random_numbers_ex = n_random_numbers(1, 3, 2)
            p.randomnumber_ex_1 = random_numbers_ex[0]
            p.randomnumber_ex_2 = random_numbers_ex[1]

            p.group_assignment = random_number(0,2) #used for randomization of the pictures

            random_numbers_questions = n_random_numbers(1, 14, 14)
            p.randomnumber_q1 = random_numbers_questions[0]
            p.randomnumber_q2 = random_numbers_questions[1]
            p.randomnumber_q3 = random_numbers_questions[2]
            p.randomnumber_q4 = random_numbers_questions[3]
            p.randomnumber_q5 = random_numbers_questions[4]
            p.randomnumber_q6 = random_numbers_questions[5]
            p.randomnumber_q7 = random_numbers_questions[6]
            p.randomnumber_q8 = random_numbers_questions[7]
            p.randomnumber_q9 = random_numbers_questions[8]
            p.randomnumber_q10 = random_numbers_questions[9]
            p.randomnumber_q11 = random_numbers_questions[10]
            p.randomnumber_q12 = random_numbers_questions[11]
            p.randomnumber_q13 = random_numbers_questions[12]
            p.randomnumber_q14 = random_numbers_questions[13]
            p.randomnumber_pop_2_2 = random_number(1, 2)
            p.randomnumber_pop_4_2 = random_number(1, 2)
            p.randomnumber_e_1_2 = random_number(1, 2)

            # input -999 for the cases in which the link is not shown in the condition
            if p.group_assignment == 0 or p.group_assignment == 2:
                p.link_check = '-999'


class Group(BaseGroup):
    def random_number(x, y):  # method for random integers
        rng = random.Random()
        number = rng.randint(x, y)
        return number


class Player(BasePlayer):
    group_assignment = models.IntegerField()
    rnumber = models.IntegerField()
    rnumbercheck = models.StringField(label="")

    ### zufällig generierte 6stellige Zufallszahl

    def rnumbercheck_error_message(self, value):
        label = self.participant.label
        number = self.rnumber
        if value != f"{label}_{number}":
            return "The confirmation code is wrong. Please try again!"
        
    feedback = models.LongStringField(blank=True)

    catdog = models.IntegerField(blank=True, max=4, min=-999, label="")
    #animal_other = models.StringField(label="Andere/Other:")
    
    time_firstendpage= models.StringField(initial="-999")
    time_endpage= models.StringField(initial="-999")

    network_narrative = models.LongStringField(blank=True)

    #time_rnumber= models.StringField(initial="-999")
    #link_check = models.StringField(blank=True)
#     randomnumber_vl_1 = models.IntegerField()
#     randomnumber_vl_2 = models.IntegerField()
#     randomnumber_tut_1 = models.IntegerField()
#     randomnumber_tut_2 = models.IntegerField()
#     randomnumber_ex_1 = models.IntegerField()
#     randomnumber_ex_2 = models.IntegerField()
#     random_numbers_questions = models.IntegerField()
#     link_check = models.StringField()

#     ###Randomnumbers definition
#     randomnumber_q1 = models.IntegerField()
#     randomnumber_q2 = models.IntegerField()
#     randomnumber_q3 = models.IntegerField()
#     randomnumber_q4 = models.IntegerField()
#     randomnumber_q5 = models.IntegerField()
#     randomnumber_q6 = models.IntegerField()
#     randomnumber_q7 = models.IntegerField()
#     randomnumber_q8 = models.IntegerField()
#     randomnumber_q9 = models.IntegerField()
#     randomnumber_q10 = models.IntegerField()
#     randomnumber_q11 = models.IntegerField()
#     randomnumber_q12 = models.IntegerField()
#     randomnumber_q13 = models.IntegerField()
#     #randomnumber_q14 =models.IntegerField()

#     #randomnumber_pop_2_2 = models.IntegerField()
#     #randomnumber_pop_4_2 = models.IntegerField()
#     #randomnumber_e_1_2 = models.IntegerField()
