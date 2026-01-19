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

# Open the file in read mode and read its lines into a list
with open('_rooms/code_list.txt', 'r') as file:
    lines = file.readlines()

# Optionally, you can remove the newline characters from each line
codes = [line.strip() for line in lines]
codes.append("x")

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'network_app'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    
    # NetworkNamedPersons fields
    person_1 = models.StringField(blank=True, label="Code 1", max_length=3, min_length=3, initial="x")
    person_2 = models.StringField(blank=True, label="Code 2", max_length=3, min_length=3, initial="x")
    person_3 = models.StringField(blank=True, label="Code 3", max_length=3, min_length=3, initial="x")
    person_4 = models.StringField(blank=True, label="Code 4", max_length=3, min_length=3, initial="x")
    person_5 = models.StringField(blank=True, label="Code 5", max_length=3, min_length=3, initial="x")
    person_6 = models.StringField(blank=True, label="Code 6", max_length=3, min_length=3, initial="x")
    person_7 = models.StringField(blank=True, label="Code 7", max_length=3, min_length=3, initial="x")
    person_8 = models.StringField(blank=True, label="Code 8", max_length=3, min_length=3, initial="x")
    person_9 = models.StringField(blank=True, label="Code 9", max_length=3, min_length=3, initial="x")
    person_10 = models.StringField(blank=True, label="Code 10", max_length=3, min_length=3, initial="x")
    person_11 = models.StringField(blank=True, label="Code 11", max_length=3, min_length=3, initial="x")
    person_12 = models.StringField(blank=True, label="Code 12", max_length=3, min_length=3, initial="x")
    person_13 = models.StringField(blank=True, label="Code 13", max_length=3, min_length=3, initial="x")
    person_14 = models.StringField(blank=True, label="Code 14", max_length=3, min_length=3, initial="x")
    person_15 = models.StringField(blank=True, label="Code 15", max_length=3, min_length=3, initial="x")
    person_16 = models.StringField(blank=True, label="Code 16", max_length=3, min_length=3, initial="x")
    person_17 = models.StringField(blank=True, label="Code 17", max_length=3, min_length=3, initial="x")
    person_18 = models.StringField(blank=True, label="Code 18", max_length=3, min_length=3, initial="x")
    person_19 = models.StringField(blank=True, label="Code 19", max_length=3, min_length=3, initial="x")
    person_20 = models.StringField(blank=True, label="Code 20", max_length=3, min_length=3, initial="x")
    person_21 = models.StringField(blank=True, label="Code 21", max_length=3, min_length=3, initial="x")
    person_22 = models.StringField(blank=True, label="Code 22", max_length=3, min_length=3, initial="x")
    person_23 = models.StringField(blank=True, label="Code 23", max_length=3, min_length=3, initial="x")
    person_24 = models.StringField(blank=True, label="Code 24", max_length=3, min_length=3, initial="x")
    person_25 = models.StringField(blank=True, label="Code 25", max_length=3, min_length=3, initial="x")
    person_26 = models.StringField(blank=True, label="Code 26", max_length=3, min_length=3, initial="x")
    person_27 = models.StringField(blank=True, label="Code 27", max_length=3, min_length=3, initial="x")
    person_28 = models.StringField(blank=True, label="Code 28", max_length=3, min_length=3, initial="x")
    person_29 = models.StringField(blank=True, label="Code 29", max_length=3, min_length=3, initial="x")
    person_30 = models.StringField(blank=True, label="Code 30", max_length=3, min_length=3, initial="x")
    person_31 = models.StringField(blank=True, label="Code 31", max_length=3, min_length=3, initial="x")
    person_32 = models.StringField(blank=True, label="Code 32", max_length=3, min_length=3, initial="x")
    person_33 = models.StringField(blank=True, label="Code 33", max_length=3, min_length=3, initial="x")
    person_34 = models.StringField(blank=True, label="Code 34", max_length=3, min_length=3, initial="x")
    person_35 = models.StringField(blank=True, label="Code 35", max_length=3, min_length=3, initial="x")
    person_36 = models.StringField(blank=True, label="Code 36", max_length=3, min_length=3, initial="x")
    person_37 = models.StringField(blank=True, label="Code 37", max_length=3, min_length=3, initial="x")
    person_38 = models.StringField(blank=True, label="Code 38", max_length=3, min_length=3, initial="x")
    person_39 = models.StringField(blank=True, label="Code 39", max_length=3, min_length=3, initial="x")
    person_40 = models.StringField(blank=True, label="Code 40", max_length=3, min_length=3, initial="x")
    person_41 = models.StringField(blank=True, label="Code 41", max_length=3, min_length=3, initial="x")
    person_42 = models.StringField(blank=True, label="Code 42", max_length=3, min_length=3, initial="x")
    person_43 = models.StringField(blank=True, label="Code 43", max_length=3, min_length=3, initial="x")
    person_44 = models.StringField(blank=True, label="Code 44", max_length=3, min_length=3, initial="x")
    person_45 = models.StringField(blank=True, label="Code 45", max_length=3, min_length=3, initial="x")
    person_46 = models.StringField(blank=True, label="Code 46", max_length=3, min_length=3, initial="x")
    person_47 = models.StringField(blank=True, label="Code 47", max_length=3, min_length=3, initial="x")
    person_48 = models.StringField(blank=True, label="Code 48", max_length=3, min_length=3, initial="x")
    person_49 = models.StringField(blank=True, label="Code 49", max_length=3, min_length=3, initial="x")
    person_50 = models.StringField(blank=True, label="Code 50", max_length=3, min_length=3, initial="x")

    def person_1_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_2_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_3_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_4_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_5_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_6_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_7_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_8_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_9_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_10_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_11_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_12_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_13_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_14_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_15_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_16_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_17_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_18_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_19_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_20_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_21_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_22_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_23_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_24_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_25_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_26_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_27_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_28_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_29_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_30_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_31_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_32_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_33_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_34_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_35_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_36_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_37_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_38_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_39_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_40_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_41_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_42_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_43_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_44_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_45_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_46_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_47_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_48_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_49_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."

    def person_50_error_message(self, value):
        if value not in codes:
            return "Please enter a valid code."


    friend_1 = models.BooleanField(blank=True, initial=False)
    old_1 = models.BooleanField(blank=True, initial=False)    
    politics_1 = models.BooleanField(blank=True, initial=False)
    study_1 = models.BooleanField(blank=True, initial=False) 
    support_1 = models.BooleanField(blank=True, initial=False)

    friend_2 = models.BooleanField(blank=True, initial=False)
    old_2 = models.BooleanField(blank=True, initial=False)    
    politics_2 = models.BooleanField(blank=True, initial=False)
    study_2 = models.BooleanField(blank=True, initial=False) 
    support_2 = models.BooleanField(blank=True, initial=False)

    friend_3 = models.BooleanField(blank=True, initial=False)
    old_3 = models.BooleanField(blank=True, initial=False)    
    politics_3 = models.BooleanField(blank=True, initial=False)
    study_3 = models.BooleanField(blank=True, initial=False) 
    support_3 = models.BooleanField(blank=True, initial=False)

    friend_4 = models.BooleanField(blank=True, initial=False)
    old_4 = models.BooleanField(blank=True, initial=False)    
    politics_4 = models.BooleanField(blank=True, initial=False)
    study_4 = models.BooleanField(blank=True, initial=False) 
    support_4 = models.BooleanField(blank=True, initial=False)

    friend_5 = models.BooleanField(blank=True, initial=False)
    old_5 = models.BooleanField(blank=True, initial=False)    
    politics_5 = models.BooleanField(blank=True, initial=False)
    study_5 = models.BooleanField(blank=True, initial=False) 
    support_5 = models.BooleanField(blank=True, initial=False)

    friend_6 = models.BooleanField(blank=True, initial=False)
    old_6 = models.BooleanField(blank=True, initial=False)    
    politics_6 = models.BooleanField(blank=True, initial=False)
    study_6 = models.BooleanField(blank=True, initial=False) 
    support_6 = models.BooleanField(blank=True, initial=False)

    friend_7 = models.BooleanField(blank=True, initial=False)
    old_7 = models.BooleanField(blank=True, initial=False)    
    politics_7 = models.BooleanField(blank=True, initial=False)
    study_7 = models.BooleanField(blank=True, initial=False) 
    support_7 = models.BooleanField(blank=True, initial=False)

    friend_8 = models.BooleanField(blank=True, initial=False)
    old_8 = models.BooleanField(blank=True, initial=False)    
    politics_8 = models.BooleanField(blank=True, initial=False)
    study_8 = models.BooleanField(blank=True, initial=False) 
    support_8 = models.BooleanField(blank=True, initial=False)

    friend_9 = models.BooleanField(blank=True, initial=False)
    old_9 = models.BooleanField(blank=True, initial=False)    
    politics_9 = models.BooleanField(blank=True, initial=False)
    study_9 = models.BooleanField(blank=True, initial=False) 
    support_9 = models.BooleanField(blank=True, initial=False)

    friend_10 = models.BooleanField(blank=True, initial=False)
    old_10 = models.BooleanField(blank=True, initial=False)    
    politics_10 = models.BooleanField(blank=True, initial=False)
    study_10 = models.BooleanField(blank=True, initial=False) 
    support_10 = models.BooleanField(blank=True, initial=False)

    friend_11 = models.BooleanField(blank=True, initial=False)
    old_11 = models.BooleanField(blank=True, initial=False)    
    politics_11 = models.BooleanField(blank=True, initial=False)
    study_11 = models.BooleanField(blank=True, initial=False) 
    support_11 = models.BooleanField(blank=True, initial=False)

    friend_12 = models.BooleanField(blank=True, initial=False)
    old_12 = models.BooleanField(blank=True, initial=False)    
    politics_12 = models.BooleanField(blank=True, initial=False)
    study_12 = models.BooleanField(blank=True, initial=False) 
    support_12 = models.BooleanField(blank=True, initial=False)

    friend_13 = models.BooleanField(blank=True, initial=False)
    old_13 = models.BooleanField(blank=True, initial=False)    
    politics_13 = models.BooleanField(blank=True, initial=False)
    study_13 = models.BooleanField(blank=True, initial=False) 
    support_13 = models.BooleanField(blank=True, initial=False)

    friend_14 = models.BooleanField(blank=True, initial=False)
    old_14 = models.BooleanField(blank=True, initial=False)    
    politics_14 = models.BooleanField(blank=True, initial=False)
    study_14 = models.BooleanField(blank=True, initial=False) 
    support_14 = models.BooleanField(blank=True, initial=False)

    friend_15 = models.BooleanField(blank=True, initial=False)
    old_15 = models.BooleanField(blank=True, initial=False)    
    politics_15 = models.BooleanField(blank=True, initial=False)
    study_15 = models.BooleanField(blank=True, initial=False) 
    support_15 = models.BooleanField(blank=True, initial=False)

    friend_16 = models.BooleanField(blank=True, initial=False)
    old_16 = models.BooleanField(blank=True, initial=False)    
    politics_16 = models.BooleanField(blank=True, initial=False)
    study_16 = models.BooleanField(blank=True, initial=False) 
    support_16 = models.BooleanField(blank=True, initial=False)

    friend_17 = models.BooleanField(blank=True, initial=False)
    old_17 = models.BooleanField(blank=True, initial=False)    
    politics_17 = models.BooleanField(blank=True, initial=False)
    study_17 = models.BooleanField(blank=True, initial=False) 
    support_17 = models.BooleanField(blank=True, initial=False)

    friend_18 = models.BooleanField(blank=True, initial=False)
    old_18 = models.BooleanField(blank=True, initial=False)    
    politics_18 = models.BooleanField(blank=True, initial=False)
    study_18 = models.BooleanField(blank=True, initial=False) 
    support_18 = models.BooleanField(blank=True, initial=False)

    friend_19 = models.BooleanField(blank=True, initial=False)
    old_19 = models.BooleanField(blank=True, initial=False)    
    politics_19 = models.BooleanField(blank=True, initial=False)
    study_19 = models.BooleanField(blank=True, initial=False) 
    support_19 = models.BooleanField(blank=True, initial=False)

    friend_20 = models.BooleanField(blank=True, initial=False)
    old_20 = models.BooleanField(blank=True, initial=False)    
    politics_20 = models.BooleanField(blank=True, initial=False)
    study_20 = models.BooleanField(blank=True, initial=False) 
    support_20 = models.BooleanField(blank=True, initial=False)

    friend_21 = models.BooleanField(blank=True, initial=False)
    old_21 = models.BooleanField(blank=True, initial=False)
    politics_21 = models.BooleanField(blank=True, initial=False)
    study_21 = models.BooleanField(blank=True, initial=False)
    support_21 = models.BooleanField(blank=True, initial=False)

    friend_22 = models.BooleanField(blank=True, initial=False)
    old_22 = models.BooleanField(blank=True, initial=False)
    politics_22 = models.BooleanField(blank=True, initial=False)
    study_22 = models.BooleanField(blank=True, initial=False)
    support_22 = models.BooleanField(blank=True, initial=False)

    friend_23 = models.BooleanField(blank=True, initial=False)
    old_23 = models.BooleanField(blank=True, initial=False)
    politics_23 = models.BooleanField(blank=True, initial=False)
    study_23 = models.BooleanField(blank=True, initial=False)
    support_23 = models.BooleanField(blank=True, initial=False)

    friend_24 = models.BooleanField(blank=True, initial=False)
    old_24 = models.BooleanField(blank=True, initial=False)
    politics_24 = models.BooleanField(blank=True, initial=False)
    study_24 = models.BooleanField(blank=True, initial=False)
    support_24 = models.BooleanField(blank=True, initial=False)

    friend_25 = models.BooleanField(blank=True, initial=False)
    old_25 = models.BooleanField(blank=True, initial=False)
    politics_25 = models.BooleanField(blank=True, initial=False)
    study_25 = models.BooleanField(blank=True, initial=False)
    support_25 = models.BooleanField(blank=True, initial=False)

    friend_26 = models.BooleanField(blank=True, initial=False)
    old_26 = models.BooleanField(blank=True, initial=False)
    politics_26 = models.BooleanField(blank=True, initial=False)
    study_26 = models.BooleanField(blank=True, initial=False)
    support_26 = models.BooleanField(blank=True, initial=False)

    friend_27 = models.BooleanField(blank=True, initial=False)
    old_27 = models.BooleanField(blank=True, initial=False)
    politics_27 = models.BooleanField(blank=True, initial=False)
    study_27 = models.BooleanField(blank=True, initial=False)
    support_27 = models.BooleanField(blank=True, initial=False)

    friend_28 = models.BooleanField(blank=True, initial=False)
    old_28 = models.BooleanField(blank=True, initial=False)
    politics_28 = models.BooleanField(blank=True, initial=False)
    study_28 = models.BooleanField(blank=True, initial=False)
    support_28 = models.BooleanField(blank=True, initial=False)

    friend_29 = models.BooleanField(blank=True, initial=False)
    old_29 = models.BooleanField(blank=True, initial=False)
    politics_29 = models.BooleanField(blank=True, initial=False)
    study_29 = models.BooleanField(blank=True, initial=False)
    support_29 = models.BooleanField(blank=True, initial=False)

    friend_30 = models.BooleanField(blank=True, initial=False)
    old_30 = models.BooleanField(blank=True, initial=False)
    politics_30 = models.BooleanField(blank=True, initial=False)
    study_30 = models.BooleanField(blank=True, initial=False)
    support_30 = models.BooleanField(blank=True, initial=False)

    friend_31 = models.BooleanField(blank=True, initial=False)
    old_31 = models.BooleanField(blank=True, initial=False)
    politics_31 = models.BooleanField(blank=True, initial=False)
    study_31 = models.BooleanField(blank=True, initial=False)
    support_31 = models.BooleanField(blank=True, initial=False)

    friend_32 = models.BooleanField(blank=True, initial=False)
    old_32 = models.BooleanField(blank=True, initial=False)
    politics_32 = models.BooleanField(blank=True, initial=False)
    study_32 = models.BooleanField(blank=True, initial=False)
    support_32 = models.BooleanField(blank=True, initial=False)

    friend_33 = models.BooleanField(blank=True, initial=False)
    old_33 = models.BooleanField(blank=True, initial=False)
    politics_33 = models.BooleanField(blank=True, initial=False)
    study_33 = models.BooleanField(blank=True, initial=False)
    support_33 = models.BooleanField(blank=True, initial=False)

    friend_34 = models.BooleanField(blank=True, initial=False)
    old_34 = models.BooleanField(blank=True, initial=False)
    politics_34 = models.BooleanField(blank=True, initial=False)
    study_34 = models.BooleanField(blank=True, initial=False)
    support_34 = models.BooleanField(blank=True, initial=False)

    friend_35 = models.BooleanField(blank=True, initial=False)
    old_35 = models.BooleanField(blank=True, initial=False)
    politics_35 = models.BooleanField(blank=True, initial=False)
    study_35 = models.BooleanField(blank=True, initial=False)
    support_35 = models.BooleanField(blank=True, initial=False)

    friend_36 = models.BooleanField(blank=True, initial=False)
    old_36 = models.BooleanField(blank=True, initial=False)
    politics_36 = models.BooleanField(blank=True, initial=False)
    study_36 = models.BooleanField(blank=True, initial=False)
    support_36 = models.BooleanField(blank=True, initial=False)

    friend_37 = models.BooleanField(blank=True, initial=False)
    old_37 = models.BooleanField(blank=True, initial=False)
    politics_37 = models.BooleanField(blank=True, initial=False)
    study_37 = models.BooleanField(blank=True, initial=False)
    support_37 = models.BooleanField(blank=True, initial=False)

    friend_38 = models.BooleanField(blank=True, initial=False)
    old_38 = models.BooleanField(blank=True, initial=False)
    politics_38 = models.BooleanField(blank=True, initial=False)
    study_38 = models.BooleanField(blank=True, initial=False)
    support_38 = models.BooleanField(blank=True, initial=False)

    friend_39 = models.BooleanField(blank=True, initial=False)
    old_39 = models.BooleanField(blank=True, initial=False)
    politics_39 = models.BooleanField(blank=True, initial=False)
    study_39 = models.BooleanField(blank=True, initial=False)
    support_39 = models.BooleanField(blank=True, initial=False)

    friend_40 = models.BooleanField(blank=True, initial=False)
    old_40 = models.BooleanField(blank=True, initial=False)
    politics_40 = models.BooleanField(blank=True, initial=False)
    study_40 = models.BooleanField(blank=True, initial=False)
    support_40 = models.BooleanField(blank=True, initial=False)

    friend_41 = models.BooleanField(blank=True, initial=False)
    old_41 = models.BooleanField(blank=True, initial=False)
    politics_41 = models.BooleanField(blank=True, initial=False)
    study_41 = models.BooleanField(blank=True, initial=False)
    support_41 = models.BooleanField(blank=True, initial=False)

    friend_42 = models.BooleanField(blank=True, initial=False)
    old_42 = models.BooleanField(blank=True, initial=False)
    politics_42 = models.BooleanField(blank=True, initial=False)
    study_42 = models.BooleanField(blank=True, initial=False)
    support_42 = models.BooleanField(blank=True, initial=False)

    friend_43 = models.BooleanField(blank=True, initial=False)
    old_43 = models.BooleanField(blank=True, initial=False)
    politics_43 = models.BooleanField(blank=True, initial=False)
    study_43 = models.BooleanField(blank=True, initial=False)
    support_43 = models.BooleanField(blank=True, initial=False)

    friend_44 = models.BooleanField(blank=True, initial=False)
    old_44 = models.BooleanField(blank=True, initial=False)
    politics_44 = models.BooleanField(blank=True, initial=False)
    study_44 = models.BooleanField(blank=True, initial=False)
    support_44 = models.BooleanField(blank=True, initial=False)

    friend_45 = models.BooleanField(blank=True, initial=False)
    old_45 = models.BooleanField(blank=True, initial=False)
    politics_45 = models.BooleanField(blank=True, initial=False)
    study_45 = models.BooleanField(blank=True, initial=False)
    support_45 = models.BooleanField(blank=True, initial=False)

    friend_46 = models.BooleanField(blank=True, initial=False)
    old_46 = models.BooleanField(blank=True, initial=False)
    politics_46 = models.BooleanField(blank=True, initial=False)
    study_46 = models.BooleanField(blank=True, initial=False)
    support_46 = models.BooleanField(blank=True, initial=False)

    friend_47 = models.BooleanField(blank=True, initial=False)
    old_47 = models.BooleanField(blank=True, initial=False)
    politics_47 = models.BooleanField(blank=True, initial=False)
    study_47 = models.BooleanField(blank=True, initial=False)
    support_47 = models.BooleanField(blank=True, initial=False)

    friend_48 = models.BooleanField(blank=True, initial=False)
    old_48 = models.BooleanField(blank=True, initial=False)
    politics_48 = models.BooleanField(blank=True, initial=False)
    study_48 = models.BooleanField(blank=True, initial=False)
    support_48 = models.BooleanField(blank=True, initial=False)

    friend_49 = models.BooleanField(blank=True, initial=False)
    old_49 = models.BooleanField(blank=True, initial=False)
    politics_49 = models.BooleanField(blank=True, initial=False)
    study_49 = models.BooleanField(blank=True, initial=False)
    support_49 = models.BooleanField(blank=True, initial=False)

    friend_50 = models.BooleanField(blank=True, initial=False)
    old_50 = models.BooleanField(blank=True, initial=False)
    politics_50 = models.BooleanField(blank=True, initial=False)
    study_50 = models.BooleanField(blank=True, initial=False)
    support_50 = models.BooleanField(blank=True, initial=False)

    group_1 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_2 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_3 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_4 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_5 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_6 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_7 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_8 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_9 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_10 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_11 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_12 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_13 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_14 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_15 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_16 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_17 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_18 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_19 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_20 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_21 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_22 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_23 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_24 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_25 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_26 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_27 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_28 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_29 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_30 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_31 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_32 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_33 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_34 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_35 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_36 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_37 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_38 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_39 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_40 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_41 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_42 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_43 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_44 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_45 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_46 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_47 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_48 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_49 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")
    group_50 = models.IntegerField(blank=True, max=50, min=0, label="(1 - 50)")

    linksrechts_self = models.IntegerField(blank=True, max=11, min=0, label="")

    linksrechts_1 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_2 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_3 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_4 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_5 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_6 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_7 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_8 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_9 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_10 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_11 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_12 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_13 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_14 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_15 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_16 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_17 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_18 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_19 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_20 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_21 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_22 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_23 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_24 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_25 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_26 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_27 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_28 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_29 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_30 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_31 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_32 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_33 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_34 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_35 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_36 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_37 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_38 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_39 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_40 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_41 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_42 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_43 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_44 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_45 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_46 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_47 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_48 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_49 = models.IntegerField(blank=True, max=11, min=0, label="")
    linksrechts_50 = models.IntegerField(blank=True, max=11, min=0, label="")

    # Timestamp tracking for NetworkNamedPersons page
    network_named_page_load_time = models.StringField(blank=True)
    network_named_page_submit_time = models.StringField(blank=True)
    network_named_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for GroupAssessment page
    group_assessment_page_load_time = models.StringField(blank=True)
    group_assessment_page_submit_time = models.StringField(blank=True)
    group_assessment_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for SpecialNetworks page
    special_networks_page_load_time = models.StringField(blank=True)
    special_networks_page_submit_time = models.StringField(blank=True)
    special_networks_page_duration_seconds = models.FloatField(blank=True)

    # Timestamp tracking for LeftrightAssessment page
    leftright_assessment_page_load_time = models.StringField(blank=True)
    leftright_assessment_page_submit_time = models.StringField(blank=True)
    leftright_assessment_page_duration_seconds = models.FloatField(blank=True)