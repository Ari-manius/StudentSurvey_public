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
Wehrdienst Vignette App - Military Service Survey
"""


class Constants(BaseConstants):
    name_in_url = 'vignett_app'
    players_per_group = None
    num_rounds = 1

    # Wehrdienst Randomization Components

    # 1. Justifications (Rechtfertigung) - 6 options
    rechtfertigung_options = {
        'russia': {'de': 'die zunehmende militärische Bedrohung durch Russland an den EU-Außengrenzen', 'en': 'the increasing military threat from Russia at the EU external borders'},
        'china': {'de': 'die wachsende globale Instabilität durch den militärischen Aufstieg Chinas', 'en': 'the growing global instability due to China\'s military rise'},
        'usa': {'de': 'die wachsenden territorialen Ambitionen und internationale Aggressivität der jetzigen US-Regierung', 'en': 'the growing territorial ambitions and international aggression of the current US government'},
        'nato': {'de': 'die zunehmende Unsicherheit über den Beistand innerhalb des NATO-Bündnisses', 'en': 'the growing uncertainty about support within the NATO alliance'},
        'leadership': {'de': 'die Notwendigkeit, dass Deutschland eine Führungsrolle in der europäischen Verteidigung übernimmt', 'en': 'the need for Germany to assume a leadership role in European defense'},
        'european_defense': {'de': 'die Notwendigkeit, dass Europa militärisch unabhängiger sein soll', 'en': 'the need for Europe to be more militarily independent'},
    }
    rechtfertigung_keys = list(rechtfertigung_options.keys())

    # 2. Target Groups (Zielgruppe) - 2 options
    zielgruppe_options = {
        'men_only': {'de': 'alle jungen Männer', 'en': 'all young men'},
        'all_adults': {'de': 'alle jungen Erwachsenen (unabhängig vom Geschlecht)', 'en': 'all young adults (regardless of gender)'},
    }
    zielgruppe_keys = list(zielgruppe_options.keys())

    # 3. Duration (Dauer) - 3 options
    dauer_options = {
        '6_months': {'de': '6 Monate', 'en': '6 months'},
        '9_months': {'de': '9 Monate', 'en': '9 months'},
        '12_months': {'de': '12 Monate', 'en': '12 months'},
    }
    dauer_keys = list(dauer_options.keys())

    # 4. Compensation (Kompensation) - 3 options
    kompensation_options = {
        'study': {
            'de': 'Wer den Wehrdienst absolviert hat, wird bei der Vergabe von zulassungsbeschränkten Studienplätzen (Numerus Clausus) bevorzugt behandelt.',
            'en': 'Those who have completed military service will be given preferential treatment in admission to restricted university programs (Numerus Clausus).'
        },
        'alternative_service': {
            'de': 'Wer keinen Wehrdienst leisten möchte, wird stattdessen zu einer deutlich längeren Sozialarbeit (Ersatzdienst) verpflichtet.',
            'en': 'Those who do not wish to perform military service will instead be required to perform significantly longer social work (alternative service).'
        },
        'payment': {
            'de': 'Der Wehrdienst wird mit deutlich mehr als 2600 Euro pro Monat kompensiert.',
            'en': 'Military service is compensated with significantly more than €2,600 per month.'
        },
    }
    kompensation_keys = list(kompensation_options.keys())


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # Wehrdienst randomization
            player.w_rechtfertigung_key = random.choice(Constants.rechtfertigung_keys)
            player.w_rechtfertigung_de = Constants.rechtfertigung_options[player.w_rechtfertigung_key]['de']
            player.w_rechtfertigung_en = Constants.rechtfertigung_options[player.w_rechtfertigung_key]['en']

            player.w_zielgruppe_key = random.choice(Constants.zielgruppe_keys)
            player.w_zielgruppe_de = Constants.zielgruppe_options[player.w_zielgruppe_key]['de']
            player.w_zielgruppe_en = Constants.zielgruppe_options[player.w_zielgruppe_key]['en']

            player.w_dauer_key = random.choice(Constants.dauer_keys)
            player.w_dauer_de = Constants.dauer_options[player.w_dauer_key]['de']
            player.w_dauer_en = Constants.dauer_options[player.w_dauer_key]['en']

            player.w_kompensation_key = random.choice(Constants.kompensation_keys)
            player.w_kompensation_de = Constants.kompensation_options[player.w_kompensation_key]['de']
            player.w_kompensation_en = Constants.kompensation_options[player.w_kompensation_key]['en']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Baseline question (7-point + no answer)
    w_baseline = models.IntegerField(blank=True, min=0, max=8, label="")

    # Affected person checkboxes
    w_affected_family = models.BooleanField(blank=True, initial=False)
    w_affected_relatives = models.BooleanField(blank=True, initial=False)
    w_affected_friends = models.BooleanField(blank=True, initial=False)
    w_affected_acquaintances = models.BooleanField(blank=True, initial=False)
    w_affected_none = models.BooleanField(blank=True, initial=False)

    # Wehrdienst vignette randomization fields
    w_rechtfertigung_key = models.StringField()
    w_rechtfertigung_de = models.StringField()
    w_rechtfertigung_en = models.StringField()

    w_zielgruppe_key = models.StringField()
    w_zielgruppe_de = models.StringField()
    w_zielgruppe_en = models.StringField()

    w_dauer_key = models.StringField()
    w_dauer_de = models.StringField()
    w_dauer_en = models.StringField()

    w_kompensation_key = models.StringField()
    w_kompensation_de = models.StringField()
    w_kompensation_en = models.StringField()

    # Post-vignette opinion (7-point + no answer)
    w_opinion = models.IntegerField(blank=True, min=0, max=8, label="")

    # Open-ended justification
    w_justification = models.LongStringField(blank=True)

    # Timestamp tracking for Intro page
    w_intro_page_load_time = models.StringField(blank=True, doc="ISO timestamp when intro page loads")
    w_intro_page_submit_time = models.StringField(blank=True, doc="ISO timestamp when intro response submitted")
    w_intro_page_duration_seconds = models.FloatField(blank=True, doc="Duration between page load and submission in seconds")

    # Timestamp tracking for vignette decision-making
    w_vignette_start_time = models.StringField(blank=True, doc="ISO timestamp when vignette page loads")
    w_vignette_submit_time = models.StringField(blank=True, doc="ISO timestamp when vignette response submitted")
    w_vignette_duration_seconds = models.FloatField(blank=True, doc="Duration between page load and submission in seconds")
