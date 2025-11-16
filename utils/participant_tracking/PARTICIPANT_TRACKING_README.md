# Participant Tracking System

## Overview

This system allows the survey to differentiate between new and returning participants, showing different pages based on their participation history.

## How It Works

### 1. Participant Identification
- Participants are identified by their **participant label** (the code assigned in the room)
- The system checks each participant's label against a list of prior participants
- Based on this check, certain pages are shown or hidden

### 2. Pages Affected

**For RETURNING participants, these pages are SKIPPED:**

**app_demographic:**
- GenderAge (age, gender)
- LevelFamily (family education level)
- Secondary (postcode, secondary school year)

**app_studium:**
- FreshersCamp (freshers camp/week attendance)
- Study (study program, semester, academic career)

**For NEW participants:**
- All pages are shown (full survey)

**For RETURNING participants:**
- Only updated questions are shown (shorter survey)

## Setup Instructions

### Step 1: Maintain the Prior Participants List

Edit the file: `prior_participants.txt`

Add one participant label per line:

```
STUDENT001
STUDENT002
STUDENT003
```

**Important:**
- Lines starting with `#` are treated as comments and ignored
- Empty lines are ignored
- Participant labels are case-sensitive
- Remove the example participants before going live!

### Step 2: Running the Survey

1. Start your oTree server as usual:
   ```bash
   otree devserver
   ```

2. When participants access the survey via the room link, the system will:
   - Check their participant label
   - Determine if they're new or returning
   - Show/hide pages accordingly

### Step 3: After Each Wave

After completing a survey wave, you can:

1. **Option A: Manual Update**
   - Export the data from oTree
   - Extract participant labels
   - Add them to `prior_participants.txt`

2. **Option B: Database Query**
   - The system could be extended to query the database directly
   - This would automatically check previous sessions

## Testing

A test script is included: `test_participant_check.py`

Run it to verify the system is working:

```bash
python test_participant_check.py
```

This will test the participant checking logic with sample data.

## Implementation Details

### Files Modified

1. **settings.py**
   - Added `is_returning_participant` to `PARTICIPANT_FIELDS`

2. **participant_utils.py** (new file)
   - Contains functions to load and check participant status

3. **app_start/pages.py**
   - Checks participant status in the `Welcome` page
   - Sets `participant.is_returning_participant` flag

4. **app_demographic/pages.py**
   - Added `is_displayed()` methods to GenderAge, LevelFamily, Secondary
   - These pages only show for new participants

5. **app_studium/pages.py**
   - Added `is_displayed()` methods to FreshersCamp, Study
   - These pages only show for new participants

6. **prior_participants.txt** (new file)
   - Stores the list of prior participant labels

### How Pages Are Controlled

Each page that should be skipped for returning participants has this method:

```python
def is_displayed(self):
    # Only show to new participants (not returning)
    return not self.participant.is_returning_participant
```

## Adding More Pages to Skip

If you want to skip additional pages for returning participants:

1. Open the relevant `pages.py` file
2. Add the `is_displayed()` method to the page class:

```python
class YourPage(Page):
    def is_displayed(self):
        return not self.participant.is_returning_participant

    # ... rest of your page code
```

## Troubleshooting

**Problem:** All participants see all pages

**Solutions:**
- Check that participant labels match exactly (case-sensitive)
- Verify `prior_participants.txt` exists and contains labels
- Check that the participant label is being set correctly in the room
- Run `test_participant_check.py` to verify the checking logic

**Problem:** No participants see the skipped pages

**Solutions:**
- Make sure `prior_participants.txt` doesn't contain all participant labels
- Check that `participant.is_returning_participant` is being set in app_start

**Problem:** Error about missing attribute

**Solutions:**
- Make sure you've added `is_returning_participant` to `PARTICIPANT_FIELDS` in settings.py
- Reset the database if you've added this to an existing project:
  ```bash
  otree resetdb
  ```

## Example Workflow

### Wave 1 (All New Participants)
1. Start with empty `prior_participants.txt` (or just comments)
2. Run survey
3. All participants see full survey
4. Export data and extract participant labels

### Wave 2 (Mix of New and Returning)
1. Add Wave 1 participant labels to `prior_participants.txt`
2. Run survey
3. Returning participants skip demographic/study background questions
4. New participants see full survey

### Wave 3+
1. Continue adding previous wave participants to the list
2. Repeat the process

## Notes

- The system is designed to be simple and maintainable
- It uses a text file for easy management
- Participant privacy is maintained (only labels are stored)
- The system is flexible and can be extended as needed
