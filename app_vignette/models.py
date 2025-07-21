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
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'vignett_app'
    players_per_group = None  
    num_rounds = 1
# English part
    text_options_part1 = ['4-year-old child', '9-year-old child', '14-year-old teenager']  #
    text_options_part2 = ['her', 'his']
    text_options_part3 = ['music', 'sports']
    text_options_part4_mapped = {
        '4-year-old child': ['kindergarten '],
        '9-year-old child': ['school '],
        '14-year-old teenager': ['school ']    }
    text_options_part5 = ['She','He']
    text_options_part6 = ['her', 'his'] 
    text_options_part7_mapped = {
        'showed a discriminatory note against': ['discriminated'],
        'committed sexual harassment': ['sexually harassed']    }
    text_options_part8_mapped = {
        'discriminated': ['discriminatory note'],
        'sexually harassed': ['harassment behavior']    }
    text_options_part9 = ['she', 'he']
    text_options_part10 = ['showed a discriminatory note against', 'committed sexual harassment']
    text_options_part11_mapped = {
        'showed a discriminatory note against' : ['Asian people', 'African people', 'South European people', 'Jewish people', 'Arab people'],
        'committed sexual harassment': ['']    }
    text_options_part12_mapped = {
        'his': ['His'],
        'her': ['Her']    }
    text_options_part13 = ['His', 'Her']
    
#German part
    g_age_child = ['Ein 4-jähriges Kind', 'Ein 9-jähriges Kind', 'Ein 14-jähriges Kind'] 
    g_age_child_mapped = {
        'Ein 4-jähriges Kind': ['4-jährigen'],
        'Ein 9-jähriges Kind': ['9-jährigen'],
        'Ein 14-jähriges Kind': ['14-jahrigen']
    }
    g_school_mapped = {
        'Ein 4-jähriges Kind': ['im Kindergarten'],
        'Ein 9-jähriges Kind': ['in der Schule'],
        'Ein 14-jähriges Kind': ['in der Schule']
    }
    g_school_mapped_2 = {
        'Ein 4-jähriges Kind': ['des Kindergartens'],
        'Ein 9-jähriges Kind': ['der Schule'],
        'Ein 14-jähriges Kind': ['der Schule']
    }
    g_school_mapped_3 = {
        'Ein 4-jähriges Kind': ['im selben Kindergarten'],
        'Ein 9-jähriges Kind': ['in derselben Schule'],
        'Ein 14-jähriges Kind': ['in derselben Schule']
    }
    g_school_mapped_4 = {
        'Ein 4-jähriges Kind': ['der Kindergarten'],
        'Ein 9-jähriges Kind': ['die Schule'],
        'Ein 14-jähriges Kind': ['die Schule']
    }

    g_gender_child = ['seinen', 'ihren']
    g_gender_child_mapped = {
        'seinen': ['Seine'],
        'ihren': ['Ihre']
    }

    g_music_sport = ['Musikkurses', 'Sportkurses']
    g_music_sport_mapped = {
        'Musikkurses': ['Musikunterricht'],
        'Sportkurses': ['Sportunterricht']
    }
    g_music_sport_mapped_2 = {
        'Musikkurses': ['Musikschule'],
        'Sportkurses': ['Sportschule']
    }
    g_director = ['dem Direktor','der Direktorin']
    g_director_mapped = {
        'dem Direktor': ['Der Direktor'],    
        'der Direktorin': ['Die Direktorin']
    }
    g_director_mapped_2 = {
        'dem Direktor': ['den Direktor'],
        'der Direktorin': ['die Direktorin']
    }
    g_director_mapped_3 = {
        'dem Direktor': ['Er'],
        'der Direktorin': ['Sie']
    }

    g_kind_of_abuse = ['sexuell übergriffiges Verhalten', 'eine diskriminierende Haltung gegenüber ']
    g_kind_of_abuse_mapped = {
        'sexuell übergriffiges Verhalten': [''],
        'eine diskriminierende Haltung gegenüber ': ['afrikanischen Menschen', 'asiatischen Menschen', 'südeuropäischen Meschen', 'jüdischen Menschen', 'arabischen Menschen']
      }
    g_kind_of_abuse_mapped_2 = {
        'sexuell übergriffiges Verhalten': ['demselben übergriffigen Verhalten'],
        'eine diskriminierende Haltung gegenüber ': ['denselben diskriminierenden Handlungen']
    }
    g_kind_of_abuse_mapped_3 = {
        'sexuell übergriffiges Verhalten': ['belästigten'],
        'eine diskriminierende Haltung gegenüber ': ['diskriminierten']
    }
    g_kind_of_abuse_mapped_4 = {
        'sexuell übergriffiges Verhalten': ['übergriffiges'],
        'eine diskriminierende Haltung gegenüber ': ['diskriminierendes']
    }

    g_gender_instructor = ['den Gruppenleiter', 'die Gruppenleiterin']
    g_gender_instructor_mapped = {
        'den Gruppenleiter': ['der Gruppenleiter sein'],
        'die Gruppenleiterin': ['die Gruppenleiterin ihr']
    }
    g_gender_instructor_mapped_2 = {
        'den Gruppenleiter': ['des Gruppenleiters'],
        'die Gruppenleiterin': ['der Gruppenleiterin']
    }
    g_gender_instructor_mapped_3 = {
        'den Gruppenleiter': ['der Gruppenleiter'],
        'die Gruppenleiterin': ['die Gruppenleiterin']
    }
    g_gender_instructor_mapped_4 = {
        'den Gruppenleiter': ['Der Gruppenleiter'],
        'die Gruppenleiterin': ['Die Gruppenleiterin']
    }

    g_gender_external_director = ['Der Direktor', 'Die Direktorin']
    g_gender_external_director_mapped = {
        'Der Direktor': ['Er'],
        'Die Direktorin': ['Sie']
    }
    g_gender_second_child = ['Ihre', 'Seine']

    
class Subsession(BaseSubsession):
    def creating_session(self):
        
        for player in self.get_players():
            player.part1 = random.choice(Constants.text_options_part1)
            player.part2 = random.choice(Constants.text_options_part2)
            player.part3 = random.choice(Constants.text_options_part3)
            player.part4 = random.choice(Constants.text_options_part4_mapped[player.part1])
            player.part9 = random.choice(Constants.text_options_part9)
            player.part5 = random.choice(Constants.text_options_part5)
            player.part6 = random.choice(Constants.text_options_part6)
            player.part10 = random.choice(Constants.text_options_part10)
            player.part7 = random.choice(Constants.text_options_part7_mapped[player.part10])
            player.part8 = random.choice(Constants.text_options_part8_mapped[player.part7])
            player.part11 = random.choice(Constants.text_options_part11_mapped[player.part10])
            player.part12 = random.choice(Constants.text_options_part12_mapped[player.part6])
            player.part13 = random.choice(Constants.text_options_part13)
            player.g_age_child = random.choice(Constants.g_age_child)
            player.g_age_child_mapped = random.choice(Constants.g_age_child_mapped[player.g_age_child])
            player.g_school_mapped = random.choice(Constants.g_school_mapped[player.g_age_child])
            player.g_school_mapped_2 = random.choice(Constants.g_school_mapped_2[player.g_age_child])
            player.g_school_mapped_3 = random.choice(Constants.g_school_mapped_3[player.g_age_child])
            player.g_school_mapped_4 = random.choice(Constants.g_school_mapped_4[player.g_age_child])
            player.g_gender_child = random.choice(Constants.g_gender_child)
            player.g_gender_child_mapped = random.choice(Constants.g_gender_child_mapped[player.g_gender_child])
            player.g_music_sport = random.choice(Constants.g_music_sport)
            player.g_music_sport_mapped = random.choice(Constants.g_music_sport_mapped[player.g_music_sport])
            player.g_music_sport_mapped_2 = random.choice(Constants.g_music_sport_mapped_2[player.g_music_sport])
            player.g_director = random.choice(Constants.g_director)
            player.g_director_mapped = random.choice(Constants.g_director_mapped[player.g_director])
            player.g_director_mapped_2 = random.choice(Constants.g_director_mapped_2[player.g_director])
            player.g_director_mapped_3 = random.choice(Constants.g_director_mapped_3[player.g_director])
            player.g_kind_of_abuse = random.choice(Constants.g_kind_of_abuse)
            player.g_kind_of_abuse_mapped = random.choice(Constants.g_kind_of_abuse_mapped[player.g_kind_of_abuse])
            player.g_kind_of_abuse_mapped_2 = random.choice(Constants.g_kind_of_abuse_mapped_2[player.g_kind_of_abuse])
            player.g_kind_of_abuse_mapped_3 = random.choice(Constants.g_kind_of_abuse_mapped_3[player.g_kind_of_abuse])
            player.g_kind_of_abuse_mapped_4 = random.choice(Constants.g_kind_of_abuse_mapped_4[player.g_kind_of_abuse])
            player.g_gender_instructor = random.choice(Constants.g_gender_instructor)
            player.g_gender_instructor_mapped = random.choice(Constants.g_gender_instructor_mapped[player.g_gender_instructor])
            player.g_gender_instructor_mapped_3 = random.choice(Constants.g_gender_instructor_mapped_3[player.g_gender_instructor])
            player.g_gender_instructor_mapped_2 = random.choice(Constants.g_gender_instructor_mapped_2[player.g_gender_instructor])
            player.g_gender_instructor_mapped_4 = random.choice(Constants.g_gender_instructor_mapped_4[player.g_gender_instructor])
            player.g_gender_external_director = random.choice(Constants.g_gender_external_director)
            player.g_gender_external_director_mapped = random.choice(Constants.g_gender_external_director_mapped[player.g_gender_external_director])
            player.g_gender_second_child = random.choice(Constants.g_gender_second_child)




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    harassment = models.IntegerField(blank=True, max=9, min=-999, label="")
    part1 = models.StringField() 
    part2 = models.StringField()
    part3 = models.StringField()  
    part4 = models.StringField()
    part9 = models.StringField()  
    part5 = models.StringField() 
    part6 = models.StringField()
    part10 = models.StringField()
    part7 = models.StringField()  
    part8 = models.StringField()  
    part11 = models.StringField()
    part12 = models.StringField()
    part13 = models.StringField()
    g_age_child = models.StringField()
    g_age_child_mapped = models.StringField()
    g_school_mapped_2 = models.StringField()
    g_school_mapped_3 = models.StringField()
    g_school_mapped_4 = models.StringField()
    g_school_mapped = models.StringField()
    g_gender_child = models.StringField()
    g_gender_child_mapped = models.StringField()
    g_music_sport = models.StringField()
    g_music_sport_mapped = models.StringField()
    g_music_sport_mapped_2 = models.StringField()
    g_director = models.StringField()
    g_director_mapped = models.StringField()
    g_director_mapped_2 = models.StringField()
    g_director_mapped_3 = models.StringField()
    g_kind_of_abuse = models.StringField()
    g_kind_of_abuse_mapped = models.StringField()
    g_kind_of_abuse_mapped_2 = models.StringField()
    g_kind_of_abuse_mapped_3 = models.StringField()
    g_kind_of_abuse_mapped_4 = models.StringField()
    g_gender_instructor = models.StringField()
    g_gender_instructor_mapped = models.StringField()
    g_gender_instructor_mapped_2 = models.StringField()
    g_gender_instructor_mapped_3 = models.StringField()
    g_gender_instructor_mapped_4 = models.StringField()
    g_gender_external_director = models.StringField()
    g_gender_external_director_mapped = models.StringField()
    g_gender_second_child = models.StringField()



