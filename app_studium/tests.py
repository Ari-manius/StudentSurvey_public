from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
import sys
import os

# Try to import LLM bot helper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils', 'bot_testing'))

try:
    from llm_bot_helper import LLMBotPersona, get_response_for_page
    USE_LLM = os.environ.get('USE_LLM_BOTS', '0') == '1'
except ImportError:
    USE_LLM = False


class PlayerBot(Bot):
    def play_round(self):
        if USE_LLM:
            # Initialize persona for consistent behavior
            persona_id = hash(str(self.participant.id_in_session)) % 5
            persona = LLMBotPersona(persona_id)
            model = os.environ.get('OLLAMA_MODEL', 'llama3.2')
        # FreshersCamp page (only if not returning participant)
        if pages.FreshersCamp.is_displayed(self):
            if USE_LLM:
                responses = get_response_for_page(
                    'FreshersCamp',
                    ['fresherscamp_student', 'freshersweek_student'],
                    'app_studium',
                    persona,
                    model
                )
                yield pages.FreshersCamp, responses
            else:
                yield pages.FreshersCamp, dict(
                    fresherscamp_student=random.randint(0, 5),
                    freshersweek_student=random.randint(0, 2)
                )

        # Study page (only if not returning participant)
        if pages.Study.is_displayed(self):
            if USE_LLM:
                responses = get_response_for_page(
                    'Study',
                    ['study_program', 'semester_of_study', 'consecutive_academic_career'],
                    'app_studium',
                    persona,
                    model
                )
                yield pages.Study, responses
            else:
                yield pages.Study, dict(
                    study_program=random.randint(0, 4),
                    semester_of_study=random.randint(1, 10),
                    consecutive_academic_career=random.randint(0, 4)
                )

        # Class page - includes self assessment and network grade assessment
        if USE_LLM:
            # Get basic responses via LLM
            responses = get_response_for_page(
                'Class',
                ['time_class', 'tutorial', 'grade'],
                'app_studium',
                persona,
                model
            )
            # Add network grade assessments (keep random for now)
            responses.update({f'grade_{i}': random.randint(0, 11) for i in range(1, 51)})
            class_data = responses
        else:
            class_data = dict(
                time_class=random.randint(0, 20),
                tutorial=random.randint(0, 8),
                grade=random.choice(['1.0', '1.3', '1.7', '2.0', '2.3', '2.7', '3.0', '3.3', '3.7', '4.0', '5.0'])
            )
            # Add network grade assessments
            class_data.update({f'grade_{i}': random.randint(0, 11) for i in range(1, 51)})

        from otree.api import Submission
        yield Submission(pages.Class, class_data, check_html=False)

        # MotivatedStrategies page
        if USE_LLM:
            responses = get_response_for_page(
                'MotivatedStrategies',
                ['motivation_intrinsic_goal_1', 'motivation_extrinsic_goal_1',
                 'motivation_intrinsic_goal_2', 'motivation_extrinsic_goal_2',
                 'motivation_intrinsic_goal_3', 'motivation_extrinsic_goal_3',
                 'motivation_extrinsic_goal_4', 'affective_academic_stress',
                 'resource_time', 'resource_peer', 'resource_help'],
                'app_studium',
                persona,
                model
            )
            yield pages.MotivatedStrategies, responses
        else:
            yield pages.MotivatedStrategies, dict(
                motivation_intrinsic_goal_1=random.randint(0, 8),
                motivation_extrinsic_goal_1=random.randint(0, 8),
                motivation_intrinsic_goal_2=random.randint(0, 8),
                motivation_extrinsic_goal_2=random.randint(0, 8),
                motivation_intrinsic_goal_3=random.randint(0, 8),
                motivation_extrinsic_goal_3=random.randint(0, 8),
                motivation_extrinsic_goal_4=random.randint(0, 8),
                affective_academic_stress=random.randint(0, 8),
                resource_time=random.randint(0, 8),
                resource_peer=random.randint(0, 8),
                resource_help=random.randint(0, 8)
            )
