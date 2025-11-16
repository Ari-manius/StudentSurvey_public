"""
Utility functions for checking participant status
"""
import os


def load_prior_participants():
    """
    Load the list of prior participants from _rooms/prior_participants.txt

    Returns:
        set: A set of participant labels who have participated before
    """
    prior_participants = set()
    # Navigate from utils/participant_tracking/ to project root, then to _rooms/
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(project_root, '_rooms', 'prior_participants.txt')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Strip whitespace and skip comments/empty lines
                line = line.strip()
                if line and not line.startswith('#'):
                    prior_participants.add(line)
    except FileNotFoundError:
        # If file doesn't exist, return empty set (all participants are new)
        pass

    return prior_participants


def is_returning_participant(participant_label):
    """
    Check if a participant label is in the prior participants list

    Args:
        participant_label: The participant's label/code

    Returns:
        bool: True if participant has participated before, False otherwise
    """
    if not participant_label:
        return False

    prior_participants = load_prior_participants()
    return participant_label in prior_participants
