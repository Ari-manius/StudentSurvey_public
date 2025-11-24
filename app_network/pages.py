from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player


class NetworkNamedPersons(Page):
    form_model = Player
    form_fields = ['person_1', 'person_2', 'person_3', 'person_4', 'person_5', 'person_6',
                   'person_7', 'person_8', 'person_9', 'person_10', 'person_11', 'person_12',
                   'person_13', 'person_14', 'person_15', 'person_16', 'person_17', 'person_18',
                   'person_19', 'person_20', 'person_21', 'person_22', 'person_23', 'person_24',
                   'person_25', 'person_26', 'person_27', 'person_28', 'person_29', 'person_30',
                   'person_31', 'person_32', 'person_33', 'person_34', 'person_35', 'person_36',
                   'person_37', 'person_38', 'person_39', 'person_40', 'person_41', 'person_42',
                   'person_43', 'person_44', 'person_45', 'person_46', 'person_47', 'person_48',
                   'person_49', 'person_50']    

    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}

class GroupAssessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['group_1', 'group_2', 'group_3', 'group_4', 'group_5', 'group_6', 'group_7', 'group_8', 'group_9', 'group_10', 'group_11',
                   'group_12', 'group_13', 'group_14', 'group_15', 'group_16', 'group_17', 'group_18', 'group_19', 'group_20', 'group_21',
                   'group_22', 'group_23', 'group_24', 'group_25', 'group_26', 'group_27', 'group_28', 'group_29', 'group_30', 'group_31',
                   'group_32', 'group_33', 'group_34', 'group_35', 'group_36', 'group_37', 'group_38', 'group_39', 'group_40', 'group_41',
                   'group_42', 'group_43', 'group_44', 'group_45', 'group_46', 'group_47', 'group_48', 'group_49', 'group_50']

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
        'friend_21', 'old_21', 'politics_21', 'support_21', 'study_21',
        'friend_22', 'old_22', 'politics_22', 'support_22', 'study_22',
        'friend_23', 'old_23', 'politics_23', 'support_23', 'study_23',
        'friend_24', 'old_24', 'politics_24', 'support_24', 'study_24',
        'friend_25', 'old_25', 'politics_25', 'support_25', 'study_25',
        'friend_26', 'old_26', 'politics_26', 'support_26', 'study_26',
        'friend_27', 'old_27', 'politics_27', 'support_27', 'study_27',
        'friend_28', 'old_28', 'politics_28', 'support_28', 'study_28',
        'friend_29', 'old_29', 'politics_29', 'support_29', 'study_29',
        'friend_30', 'old_30', 'politics_30', 'support_30', 'study_30',
        'friend_31', 'old_31', 'politics_31', 'support_31', 'study_31',
        'friend_32', 'old_32', 'politics_32', 'support_32', 'study_32',
        'friend_33', 'old_33', 'politics_33', 'support_33', 'study_33',
        'friend_34', 'old_34', 'politics_34', 'support_34', 'study_34',
        'friend_35', 'old_35', 'politics_35', 'support_35', 'study_35',
        'friend_36', 'old_36', 'politics_36', 'support_36', 'study_36',
        'friend_37', 'old_37', 'politics_37', 'support_37', 'study_37',
        'friend_38', 'old_38', 'politics_38', 'support_38', 'study_38',
        'friend_39', 'old_39', 'politics_39', 'support_39', 'study_39',
        'friend_40', 'old_40', 'politics_40', 'support_40', 'study_40',
        'friend_41', 'old_41', 'politics_41', 'support_41', 'study_41',
        'friend_42', 'old_42', 'politics_42', 'support_42', 'study_42',
        'friend_43', 'old_43', 'politics_43', 'support_43', 'study_43',
        'friend_44', 'old_44', 'politics_44', 'support_44', 'study_44',
        'friend_45', 'old_45', 'politics_45', 'support_45', 'study_45',
        'friend_46', 'old_46', 'politics_46', 'support_46', 'study_46',
        'friend_47', 'old_47', 'politics_47', 'support_47', 'study_47',
        'friend_48', 'old_48', 'politics_48', 'support_48', 'study_48',
        'friend_49', 'old_49', 'politics_49', 'support_49', 'study_49',
        'friend_50', 'old_50', 'politics_50', 'support_50', 'study_50']              
                   
class LeftrightAssessment(Page):
    form_model = Player
    form_fields = ['linksrechts_self',
                   'linksrechts_1', 'linksrechts_2', 'linksrechts_3', 'linksrechts_4', 'linksrechts_5', 'linksrechts_6', 'linksrechts_7', 'linksrechts_8', 'linksrechts_9', 'linksrechts_10', 'linksrechts_11',
                   'linksrechts_12', 'linksrechts_13', 'linksrechts_14', 'linksrechts_15', 'linksrechts_16', 'linksrechts_17', 'linksrechts_18', 'linksrechts_19', 'linksrechts_20', 'linksrechts_21',
                   'linksrechts_22', 'linksrechts_23', 'linksrechts_24', 'linksrechts_25', 'linksrechts_26', 'linksrechts_27', 'linksrechts_28', 'linksrechts_29', 'linksrechts_30', 'linksrechts_31',
                   'linksrechts_32', 'linksrechts_33', 'linksrechts_34', 'linksrechts_35', 'linksrechts_36', 'linksrechts_37', 'linksrechts_38', 'linksrechts_39', 'linksrechts_40', 'linksrechts_41',
                   'linksrechts_42', 'linksrechts_43', 'linksrechts_44', 'linksrechts_45', 'linksrechts_46', 'linksrechts_47', 'linksrechts_48', 'linksrechts_49', 'linksrechts_50']
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}

page_sequence = [NetworkNamedPersons, SpecialNetworks, GroupAssessment, LeftrightAssessment] 