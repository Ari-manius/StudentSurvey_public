from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class Participantcode(Page): #2
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['participantcode']

class NetworkNamedPersons(Page):
    form_model = Player
    form_fields = ['person_1', 'person_2', 'person_3', 'person_4', 'person_5', 'person_6',
                   'person_7', 'person_8', 'person_9', 'person_10', 'person_11', 'person_12',
                   'person_13', 'person_14', 'person_15', 'person_16', 'person_17', 'person_18',
                   'person_19', 'person_20', 'person_21', 'person_22', 'person_23', 'person_24',
                   'person_25', 'person_26', 'person_27', 'person_28', 'person_29', 'person_30']    

    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}


class LeftrightNetworkAssessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['linksrechts_1', 'linksrechts_2', 'linksrechts_3', 'linksrechts_4', 'linksrechts_5', 'linksrechts_6', 'linksrechts_7', 'linksrechts_8', 'linksrechts_9', 'linksrechts_10', 'linksrechts_11',
                   'linksrechts_12', 'linksrechts_13', 'linksrechts_14', 'linksrechts_15', 'linksrechts_16', 'linksrechts_17', 'linksrechts_18', 'linksrechts_19', 'linksrechts_20', 'linksrechts_21',
                   'linksrechts_22', 'linksrechts_23', 'linksrechts_24', 'linksrechts_25', 'linksrechts_26', 'linksrechts_27', 'linksrechts_28', 'linksrechts_29', 'linksrechts_30']

class SentimentAssesment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['sentiment_1', 'sentiment_2', 'sentiment_3', 'sentiment_4', 'sentiment_5', 'sentiment_6', 'sentiment_7', 'sentiment_8', 'sentiment_9', 'sentiment_10', 'sentiment_11',
                   'sentiment_12', 'sentiment_13', 'sentiment_14', 'sentiment_15', 'sentiment_16', 'sentiment_17', 'sentiment_18', 'sentiment_19', 'sentiment_20', 'sentiment_21',
                   'sentiment_22', 'sentiment_23', 'sentiment_24', 'sentiment_25', 'sentiment_26', 'sentiment_27', 'sentiment_28', 'sentiment_29', 'sentiment_30']

class LeftrightSelfAssessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['linksrechts_self']

class SpecialNetworks(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = [
        'friend_1', 'value_1', 'politics_1', 'council_1', 'study_1',
        'friend_2', 'value_2', 'politics_2', 'council_2', 'study_2',
        'friend_3', 'value_3', 'politics_3', 'council_3', 'study_3',
        'friend_4', 'value_4', 'politics_4', 'council_4', 'study_4',
        'friend_5', 'value_5', 'politics_5', 'council_5', 'study_5',
        'friend_6', 'value_6', 'politics_6', 'council_6', 'study_6',
        'friend_7', 'value_7', 'politics_7', 'council_7', 'study_7',
        'friend_8', 'value_8', 'politics_8', 'council_8', 'study_8',
        'friend_9', 'value_9', 'politics_9', 'council_9', 'study_9',
        'friend_10', 'value_10', 'politics_10', 'council_10', 'study_10',
        'friend_11', 'value_11', 'politics_11', 'council_11', 'study_11',
        'friend_12', 'value_12', 'politics_12', 'council_12', 'study_12',
        'friend_13', 'value_13', 'politics_13', 'council_13', 'study_13',
        'friend_14', 'value_14', 'politics_14', 'council_14', 'study_14',
        'friend_15', 'value_15', 'politics_15', 'council_15', 'study_15',
        'friend_16', 'value_16', 'politics_16', 'council_16', 'study_16',
        'friend_17', 'value_17', 'politics_17', 'council_17', 'study_17',
        'friend_18', 'value_18', 'politics_18', 'council_18', 'study_18',
        'friend_19', 'value_19', 'politics_19', 'council_19', 'study_19',
        'friend_20', 'value_20', 'politics_20', 'council_20', 'study_20',
        'friend_21', 'value_21', 'politics_21', 'council_21', 'study_21',
        'friend_22', 'value_22', 'politics_22', 'council_22', 'study_22',
        'friend_23', 'value_23', 'politics_23', 'council_23', 'study_23',
        'friend_24', 'value_24', 'politics_24', 'council_24', 'study_24',
        'friend_25', 'value_25', 'politics_25', 'council_25', 'study_25',
        'friend_26', 'value_26', 'politics_26', 'council_26', 'study_26',
        'friend_27', 'value_27', 'politics_27', 'council_27', 'study_27',
        'friend_28', 'value_28', 'politics_28', 'council_28', 'study_28',
        'friend_29', 'value_29', 'politics_29', 'council_29', 'study_29',
        'friend_30', 'value_30', 'politics_30', 'council_30', 'study_30']              
 
                   
page_sequence = [NetworkNamedPersons, SpecialNetworks, SentimentAssesment, LeftrightSelfAssessment ,LeftrightNetworkAssessment] 

# docker compose up -d --build 