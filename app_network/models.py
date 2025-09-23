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
    ### Participant Code
    participantcode = models.StringField(blank=False, label="Participant Code")

    def participantcode_error_message(self, value):
        # Check if the input is exactly 3 letters long and contains only alphanumeric characters
        label = self.participant.label

        # Check if the code is in the allowed list and not the same as their own
        if value not in codes:
            return "This code is not a valid code."

        if value == label:
            return "You cannot enter your own code."
    
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


    friend_1 = models.BooleanField(blank=True, initial=False)
    value_1 = models.BooleanField(blank=True, initial=False)    
    politics_1 = models.BooleanField(blank=True, initial=False)
    study_1 = models.BooleanField(blank=True, initial=False) 
    council_1 = models.BooleanField(blank=True, initial=False)

    friend_2 = models.BooleanField(blank=True, initial=False)
    value_2 = models.BooleanField(blank=True, initial=False)    
    politics_2 = models.BooleanField(blank=True, initial=False)
    study_2 = models.BooleanField(blank=True, initial=False) 
    council_2 = models.BooleanField(blank=True, initial=False)

    friend_3 = models.BooleanField(blank=True, initial=False)
    value_3 = models.BooleanField(blank=True, initial=False)    
    politics_3 = models.BooleanField(blank=True, initial=False)
    study_3 = models.BooleanField(blank=True, initial=False) 
    council_3 = models.BooleanField(blank=True, initial=False)

    friend_4 = models.BooleanField(blank=True, initial=False)
    value_4 = models.BooleanField(blank=True, initial=False)    
    politics_4 = models.BooleanField(blank=True, initial=False)
    study_4 = models.BooleanField(blank=True, initial=False) 
    council_4 = models.BooleanField(blank=True, initial=False)

    friend_5 = models.BooleanField(blank=True, initial=False)
    value_5 = models.BooleanField(blank=True, initial=False)    
    politics_5 = models.BooleanField(blank=True, initial=False)
    study_5 = models.BooleanField(blank=True, initial=False) 
    council_5 = models.BooleanField(blank=True, initial=False)

    friend_6 = models.BooleanField(blank=True, initial=False)
    value_6 = models.BooleanField(blank=True, initial=False)    
    politics_6 = models.BooleanField(blank=True, initial=False)
    study_6 = models.BooleanField(blank=True, initial=False) 
    council_6 = models.BooleanField(blank=True, initial=False)

    friend_7 = models.BooleanField(blank=True, initial=False)
    value_7 = models.BooleanField(blank=True, initial=False)    
    politics_7 = models.BooleanField(blank=True, initial=False)
    study_7 = models.BooleanField(blank=True, initial=False) 
    council_7 = models.BooleanField(blank=True, initial=False)

    friend_8 = models.BooleanField(blank=True, initial=False)
    value_8 = models.BooleanField(blank=True, initial=False)    
    politics_8 = models.BooleanField(blank=True, initial=False)
    study_8 = models.BooleanField(blank=True, initial=False) 
    council_8 = models.BooleanField(blank=True, initial=False)

    friend_9 = models.BooleanField(blank=True, initial=False)
    value_9 = models.BooleanField(blank=True, initial=False)    
    politics_9 = models.BooleanField(blank=True, initial=False)
    study_9 = models.BooleanField(blank=True, initial=False) 
    council_9 = models.BooleanField(blank=True, initial=False)

    friend_10 = models.BooleanField(blank=True, initial=False)
    value_10 = models.BooleanField(blank=True, initial=False)    
    politics_10 = models.BooleanField(blank=True, initial=False)
    study_10 = models.BooleanField(blank=True, initial=False) 
    council_10 = models.BooleanField(blank=True, initial=False)

    friend_11 = models.BooleanField(blank=True, initial=False)
    value_11 = models.BooleanField(blank=True, initial=False)    
    politics_11 = models.BooleanField(blank=True, initial=False)
    study_11 = models.BooleanField(blank=True, initial=False) 
    council_11 = models.BooleanField(blank=True, initial=False)

    friend_12 = models.BooleanField(blank=True, initial=False)
    value_12 = models.BooleanField(blank=True, initial=False)    
    politics_12 = models.BooleanField(blank=True, initial=False)
    study_12 = models.BooleanField(blank=True, initial=False) 
    council_12 = models.BooleanField(blank=True, initial=False)

    friend_13 = models.BooleanField(blank=True, initial=False)
    value_13 = models.BooleanField(blank=True, initial=False)    
    politics_13 = models.BooleanField(blank=True, initial=False)
    study_13 = models.BooleanField(blank=True, initial=False) 
    council_13 = models.BooleanField(blank=True, initial=False)

    friend_14 = models.BooleanField(blank=True, initial=False)
    value_14 = models.BooleanField(blank=True, initial=False)    
    politics_14 = models.BooleanField(blank=True, initial=False)
    study_14 = models.BooleanField(blank=True, initial=False) 
    council_14 = models.BooleanField(blank=True, initial=False)

    friend_15 = models.BooleanField(blank=True, initial=False)
    value_15 = models.BooleanField(blank=True, initial=False)    
    politics_15 = models.BooleanField(blank=True, initial=False)
    study_15 = models.BooleanField(blank=True, initial=False) 
    council_15 = models.BooleanField(blank=True, initial=False)

    friend_16 = models.BooleanField(blank=True, initial=False)
    value_16 = models.BooleanField(blank=True, initial=False)    
    politics_16 = models.BooleanField(blank=True, initial=False)
    study_16 = models.BooleanField(blank=True, initial=False) 
    council_16 = models.BooleanField(blank=True, initial=False)

    friend_17 = models.BooleanField(blank=True, initial=False)
    value_17 = models.BooleanField(blank=True, initial=False)    
    politics_17 = models.BooleanField(blank=True, initial=False)
    study_17 = models.BooleanField(blank=True, initial=False) 
    council_17 = models.BooleanField(blank=True, initial=False)

    friend_18 = models.BooleanField(blank=True, initial=False)
    value_18 = models.BooleanField(blank=True, initial=False)    
    politics_18 = models.BooleanField(blank=True, initial=False)
    study_18 = models.BooleanField(blank=True, initial=False) 
    council_18 = models.BooleanField(blank=True, initial=False)

    friend_19 = models.BooleanField(blank=True, initial=False)
    value_19 = models.BooleanField(blank=True, initial=False)    
    politics_19 = models.BooleanField(blank=True, initial=False)
    study_19 = models.BooleanField(blank=True, initial=False) 
    council_19 = models.BooleanField(blank=True, initial=False)

    friend_20 = models.BooleanField(blank=True, initial=False)
    value_20 = models.BooleanField(blank=True, initial=False)    
    politics_20 = models.BooleanField(blank=True, initial=False)
    study_20 = models.BooleanField(blank=True, initial=False) 
    council_20 = models.BooleanField(blank=True, initial=False)

    friend_21 = models.BooleanField(blank=True, initial=False)
    value_21 = models.BooleanField(blank=True, initial=False)    
    politics_21 = models.BooleanField(blank=True, initial=False)
    study_21 = models.BooleanField(blank=True, initial=False) 
    council_21 = models.BooleanField(blank=True, initial=False)

    linksrechts_1 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_2 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_3 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_4 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_5 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_6 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_7 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_8 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_9 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_10 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_11 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_12 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_13 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_14 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_15 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_16 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_17 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_18 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_19 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_20 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_21 = models.IntegerField(blank=True, max=11, min=1, label="")

    sentiment_1 = models.IntegerField(blank=True, max=2, min=-2, label="", )
    sentiment_2 = models.IntegerField(blank=True, max=2, min=-2, label="", )
    sentiment_3 = models.IntegerField(blank=True, max=2, min=-2, label="", )
    sentiment_4 = models.IntegerField(blank=True, max=2, min=-2, label="", )
    sentiment_5 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_6 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_7 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_8 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_9 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_10 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_11 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_12 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_13 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_14 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_15 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_16 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_17 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_18 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_19 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_20 = models.IntegerField(blank=True, max=2, min=-2, label="")
    sentiment_21 = models.IntegerField(blank=True, max=2, min=-2, label="")

    grade_1 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_2 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_3 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_4 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_5 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_6 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_7 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_8 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_9 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_10 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_11 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_12 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_13 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_14 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_15 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_16 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_17 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_18 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_19 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_20 = models.IntegerField(blank=True, max=11, min=1, label="")
    grade_21 = models.IntegerField(blank=True, max=11, min=1, label="")