import os
import sys

print("Verifying participant tracking setup...")
print("-" * 60)

# Check files exist
project_root = os.path.dirname(os.path.abspath(__file__))
print(f"Project root: {project_root}")

files_to_check = [
    "_rooms/prior_participants.txt",
    "utils/__init__.py",
    "utils/participant_tracking/__init__.py",
    "utils/participant_tracking/participant_utils.py"
]

for file_path in files_to_check:
    full_path = os.path.join(project_root, file_path)
    exists = os.path.exists(full_path)
    status = "✓" if exists else "✗"
    print(f"{status} {file_path}: {'EXISTS' if exists else 'MISSING'}")

print("-" * 60)

# Try importing
try:
    sys.path.insert(0, project_root)
    from utils.participant_tracking.participant_utils import is_returning_participant, load_prior_participants
    print("✓ Import successful")

    # Try loading participants
    participants = load_prior_participants()
    print(f"✓ Loaded {len(participants)} prior participant(s): {participants}")

    # Test function
    result = is_returning_participant("cav")
    print(f"✓ Function works: is_returning_participant('cav') = {result}")

    print("\n✓ ALL CHECKS PASSED - System is ready!")

except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
