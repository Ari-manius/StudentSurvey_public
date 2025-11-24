# oTree Bot Testing for Student Survey WS 25/26

## Overview

This project includes comprehensive bot testing scripts to simulate participants taking the OTRE survey. Bot tests are automated scripts that fill out the survey with random (but valid) data to test the survey flow and ensure all pages work correctly.

## What Was Created

### 1. Individual App Test Files

Bot test files have been created/updated for each app in the survey:

- `app_start/tests.py` - Tests the welcome page with language selection, device info, etc.
- `app_demographic/tests.py` - Tests demographic questions (age, gender, education, financial situation)
- `app_studium/tests.py` - Tests study-related questions (program, semester, class, motivation)
- `app_network/tests.py` - Tests the extensive network module (50 persons with multiple attributes)
- `app_migration/tests.py` - Tests migration-related pages
- `app_political/tests.py` - Tests political questions (party preferences, political participation)
- `app_end/tests.py` - Tests final pages (feedback, random number verification)

### 2. Main Bot Runner Script

`run-otree-bot-test.py` - A comprehensive script that:
- Runs bots through the entire survey
- Exports results to CSV files for analysis
- Preserves your existing database by creating a temporary test database

## How The Bots Work

Each bot (`PlayerBot` class) simulates a participant by:

1. **Generating realistic random data** within the valid ranges for each field
2. **Respecting conditional logic** (e.g., only showing certain pages to new vs. returning participants)
3. **Following the page sequence** defined in each app

### Example from `app_start/tests.py`:

```python
yield pages.Welcome, dict(
    lang=random.choice([0, 1]),  # Random language selection
    time=str(random.randint(10, 30)),  # Random time
    device_type=random.randint(0, 2),  # Random device
    # ... etc
)
```

## Running the Bot Tests

### Method 1: Using the custom runner (Recommended) ✅

**Important:** Use Python 3.11 with the otree virtual environment:

```bash
cd /path/to/StudentSurvey_WS2526

# Make sure you're using Python 3.11 with oTree venv
pyenv local 3.11.9/envs/otree_venv_3.11

# Run the bot test
python run-otree-bot-test.py
```

This will:
- Run 10 bot participants through the survey
- Export results to `bot_test_results/` directory
- Generate CSV files for each app including:
  - `all_apps_wide.csv` - Complete survey data in wide format
  - Individual app CSV files (`app_start.csv`, `app_demographic.csv`, etc.)

**Expected output:**
```
Creating 'SS_WS2526' session (test case 0)
Submit /p/xxxxx/start/Welcome/1, {...}
...
Bots completed session
Exported CSV to folder "bot_test_results"
Bot test completed successfully!
Results exported to: bot_test_results/
```

### Method 2: Using oTree's built-in command

```bash
otree test SS_WS2526
```

**Note:** Python 3.11 is required. Python 3.13 has SQLAlchemy compatibility issues with the current oTree version.

## What Gets Tested

The bots test:

- ✅ All form fields accept valid data
- ✅ Page transitions work correctly
- ✅ Conditional page display logic (returning vs. new participants)
- ✅ Data validation rules
- ✅ The complete survey flow from start to finish

## Data Generated

The bots generate realistic random data:

- **Integer fields**: Random values within min/max constraints
- **String fields**: Random selections from appropriate options
- **Boolean fields**: Random True/False values
- **Network data**: Properly formatted person codes and relationship indicators

## Troubleshooting

### Python Version Error

If you get a SQLAlchemy error about "Textual column expression 'id'", you're likely using Python 3.13. Switch to Python 3.11:

```bash
cd /path/to/StudentSurvey_WS2526
pyenv local 3.11.9/envs/otree_venv_3.11
python run-otree-bot-test.py
```

### Missing Dependencies

If you get "You need to install requests":

```bash
/Users/ramius/.pyenv/versions/3.11.9/envs/otree_venv_3.11/bin/pip install requests
```

### Database Migration Needed

If you see "oTree has been updated. Please delete your database":

```bash
rm db.sqlite3
otree resetdb
```

### Bot Test Successful! ✅

If you see this output, everything worked:
```
Bots completed session
Exported CSV to folder "bot_test_results"
Bot test completed successfully!
Results exported to: bot_test_results/
```

Check the `bot_test_results/` folder for your exported data.

## Modifying the Bots

To adjust bot behavior:

1. **Change number of participants**: Edit `num_participants` in `run-otree-bot-test.py`
2. **Adjust random data ranges**: Edit the individual `tests.py` files in each app
3. **Add custom validation**: Extend the `PlayerBot.play_round()` methods

## Files Structure

```
StudentSurvey_WS2526/
├── run-otree-bot-test.py          # Main runner script
├── app_start/tests.py              # Start app bot tests
├── app_demographic/tests.py        # Demographic bot tests
├── app_studium/tests.py            # Study questions bot tests
├── app_network/tests.py            # Network module bot tests (most complex)
├── app_migration/tests.py          # Migration bot tests
├── app_political/tests.py          # Political questions bot tests
├── app_end/tests.py                # End pages bot tests
└── bot_test_results/               # Output directory (created after running)
```

## Benefits of Bot Testing

1. **Quick validation** - Test the entire survey in seconds instead of manually clicking through
2. **Regression testing** - Ensure changes don't break existing functionality
3. **Data generation** - Create test datasets for analysis code development
4. **Edge case testing** - Bots can test many scenarios quickly

## Next Steps

1. Fix the SQLAlchemy compatibility issue (if needed)
2. Run the bots and verify all pages work
3. Examine the exported CSV files
4. Adjust bot behavior if needed for more realistic test data
