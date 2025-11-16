"""
Test script to verify participant tracking system works correctly
Run this from the project root directory
"""
from utils.participant_tracking.participant_utils import is_returning_participant, load_prior_participants


def test_participant_checking():
    """Test the participant checking logic"""

    print("=" * 60)
    print("Testing Participant Tracking System")
    print("=" * 60)

    # Load prior participants
    prior_participants = load_prior_participants()
    print(f"\nPrior participants loaded from _rooms/: {prior_participants}")

    # Test cases - based on current prior_participants.txt
    test_cases = [
        ("cav", True),          # Should be returning (in the list)
        ("STUDENT001", False),  # Should be new (not in the list)
        ("STUDENT002", False),  # Should be new (not in the list)
        ("NEWSTUDENT", False),  # Should be new
        ("", False),            # Empty should be new
        (None, False),          # None should be new
    ]

    print("\n" + "-" * 60)
    print("Test Results:")
    print("-" * 60)

    all_passed = True
    for participant_label, expected_returning in test_cases:
        result = is_returning_participant(participant_label)
        status = "PASS" if result == expected_returning else "FAIL"

        if status == "FAIL":
            all_passed = False

        print(f"{status}: Label '{participant_label}' -> "
              f"Returning: {result} (Expected: {expected_returning})")

    print("-" * 60)
    if all_passed:
        print("\nAll tests PASSED!")
        print("\nThe participant tracking system is working correctly:")
        print("- Loads participant list from _rooms/prior_participants.txt")
        print("- Correctly identifies returning vs new participants")
        print("- Ready to use in your survey")
    else:
        print("\nSome tests FAILED!")
        print("Please check the prior_participants.txt file")
    print("=" * 60)

    return all_passed


if __name__ == "__main__":
    test_participant_checking()
