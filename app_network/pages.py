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
                   'person_19', 'person_20', 'person_21']    

    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}

class AcademicNetworkAssessment(Page): #8
    form_model = Player
    form_fields = ['grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10', 'grade_11',
                   'grade_12', 'grade_13', 'grade_14', 'grade_15', 'grade_16', 'grade_17', 'grade_18', 'grade_19', 'grade_20', 'grade_21']
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}

class GroupAssessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['group_1', 'group_2', 'group_3', 'group_4', 'group_5', 'group_6', 'group_7', 'group_8', 'group_9', 'group_10', 'group_11',
                   'group_12', 'group_13', 'group_14', 'group_15', 'group_16', 'group_17', 'group_18', 'group_19', 'group_20', 'group_21']

class SentimentAssessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['sentiment_1', 'sentiment_2', 'sentiment_3', 'sentiment_4', 'sentiment_5', 'sentiment_6', 'sentiment_7', 'sentiment_8', 'sentiment_9', 'sentiment_10', 'sentiment_11',
                   'sentiment_12', 'sentiment_13', 'sentiment_14', 'sentiment_15', 'sentiment_16', 'sentiment_17', 'sentiment_18', 'sentiment_19', 'sentiment_20', 'sentiment_21']

class SpecialNetworks(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = [
        'friend_1', 'old_1', 'politics_1', 'support_1', 'study_1',
        'friend_2', 'old_2', 'politics_2', 'support_2', 'study_2',
        'friend_3', 'old_3', 'politics_3', 'support_3', 'study_3',
        'friend_4', 'old_4', 'politics_4', 'support_4', 'study_4',
        'friend_5', 'old_5', 'politics_5', 'support_5', 'study_5',
        'friend_6', 'old_6', 'politics_6', 'support_6', 'study_6',
        'friend_7', 'old_7', 'politics_7', 'support_7', 'study_7',
        'friend_8', 'old_8', 'politics_8', 'support_8', 'study_8',
        'friend_9', 'old_9', 'politics_9', 'support_9', 'study_9',
        'friend_10', 'old_10', 'politics_10', 'support_10', 'study_10',
        'friend_11', 'old_11', 'politics_11', 'support_11', 'study_11',
        'friend_12', 'old_12', 'politics_12', 'support_12', 'study_12',
        'friend_13', 'old_13', 'politics_13', 'support_13', 'study_13',
        'friend_14', 'old_14', 'politics_14', 'support_14', 'study_14',
        'friend_15', 'old_15', 'politics_15', 'support_15', 'study_15',
        'friend_16', 'old_16', 'politics_16', 'support_16', 'study_16',
        'friend_17', 'old_17', 'politics_17', 'support_17', 'study_17',
        'friend_18', 'old_18', 'politics_18', 'support_18', 'study_18',
        'friend_19', 'old_19', 'politics_19', 'support_19', 'study_19',
        'friend_20', 'old_20', 'politics_20', 'support_20', 'study_20',
        'friend_21', 'old_21', 'politics_21', 'support_21', 'study_21']              
 
class NetworkNarrative(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ["network_narrative"]
                   
class LeftrightSelfAssessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['linksrechts_self']

class LeftrightNetworkAssessment(Page): #8
    form_model = Player
    form_fields = ['linksrechts_1', 'linksrechts_2', 'linksrechts_3', 'linksrechts_4', 'linksrechts_5', 'linksrechts_6', 'linksrechts_7', 'linksrechts_8', 'linksrechts_9', 'linksrechts_10', 'linksrechts_11',
                   'linksrechts_12', 'linksrechts_13', 'linksrechts_14', 'linksrechts_15', 'linksrechts_16', 'linksrechts_17', 'linksrechts_18', 'linksrechts_19', 'linksrechts_20', 'linksrechts_21']
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}


page_sequence = [NetworkNamedPersons, SpecialNetworks, GroupAssessment, AcademicNetworkAssessment, NetworkNarrative, LeftrightSelfAssessment, LeftrightNetworkAssessment] 