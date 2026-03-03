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
    name_in_url = 'app_AI'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    AI_use_1 = models.IntegerField(blank=True, max=1, min=0, label="") #Allgemeine Informationssuche
    AI_use_2 = models.IntegerField(blank=True, max=1, min=0, label="") #Verständnis von Vorlesungsskripten oder Fachtexten
    AI_use_3 = models.IntegerField(blank=True, max=1, min=0, label="") #Beantwortung von Übungsblätter im Tutorat
    AI_use_4 = models.IntegerField(blank=True, max=1, min=0, label="") #Beantwortung von Quizfragen
    AI_use_5 = models.IntegerField(blank=True, max=1, min=0, label="") #Vorbereitung auf Klausuren oder Prüfungen
    AI_use_no = models.IntegerField(blank=True, max=1, min=0, label="") #No Use
    AI_use_other = models.LongStringField(blank=True) #Andere/Other

    AI_tool_1 = models.IntegerField(blank=True, max=1, min=0, label="") # ChatGPT
    AI_tool_2 = models.IntegerField(blank=True, max=1, min=0, label="") # Gemini
    AI_tool_3 = models.IntegerField(blank=True, max=1, min=0, label="") # Perplexity
    AI_tool_4 = models.IntegerField(blank=True, max=1, min=0, label="") # Claude
    AI_tool_5 = models.IntegerField(blank=True, max=1, min=0, label="") # Grok
    AI_tool_no = models.IntegerField(blank=True, max=1, min=0, label="")
    AI_tool_other = models.LongStringField(blank=True)

    AI_subscription = models.IntegerField(blank=True, max=2, min=0, label="")

    AI_prompt = models.LongStringField(blank=True)

    AI_use_other = models.LongStringField(blank=True)

    # Timestamp tracking for AI_use page
    ai_page_load_time = models.StringField(blank=True, doc="ISO timestamp when AI_use page loads")
    ai_page_submit_time = models.StringField(blank=True, doc="ISO timestamp when AI_use response submitted")
    ai_page_duration_seconds = models.FloatField(blank=True, doc="Duration in seconds")