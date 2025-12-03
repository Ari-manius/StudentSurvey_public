#!/usr/bin/env python3
"""
Ollama LLM-Powered Bot Testing Script

This script runs oTree bot tests using Ollama LLM to generate realistic responses
instead of random values.

Prerequisites:
1. Install ollama: https://ollama.ai/
2. Start ollama server: ollama serve
3. Pull a model: ollama pull llama3.2
4. Install Python package: pip install ollama

Usage:
    # Local testing with LLM bots (default 10 participants)
    python utils/bot_testing/run-otree-bot-test-llm.py

    # Specify number of participants
    python utils/bot_testing/run-otree-bot-test-llm.py 20

    # Use different model
    OLLAMA_MODEL=llama3.1 python utils/bot_testing/run-otree-bot-test-llm.py

    # Check if Ollama is available
    python utils/bot_testing/run-otree-bot-test-llm.py --check

Note: LLM-based testing is MUCH slower than random testing due to LLM inference time.
      Expect ~1-5 seconds per question per participant depending on your hardware.
"""

import os
import sys


def check_ollama():
    """Check if Ollama is installed and running"""
    print("Checking Ollama setup...")

    # Check if ollama package is installed
    try:
        import ollama
        print("✓ ollama Python package installed")
    except ImportError:
        print("✗ ollama Python package NOT installed")
        print("  Install with: pip install ollama")
        return False

    # Check if Ollama server is running
    try:
        import ollama as client
        models_response = client.list()
        print("✓ Ollama server is running")

        # List available models
        if models_response and 'models' in models_response and models_response['models']:
            print("\nAvailable models:")
            for model in models_response['models']:
                # Handle different response formats
                model_name = model.get('name') or model.get('model') or str(model)
                print(f"  - {model_name}")
        else:
            print("\n✗ No models found")
            print("  Pull a model with: ollama pull llama3.2")
            return False

        return True

    except Exception as e:
        print("✗ Ollama server NOT running or not accessible")
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        print("  Start with: ollama serve")
        return False


def setup_llm_tests():
    """
    Dynamically patch test files to use LLM responses

    This modifies the bot behavior at runtime without changing the original test files.
    """
    print("\nSetting up LLM-powered bot tests...")

    # Import the helper
    sys.path.insert(0, os.path.dirname(__file__))

    try:
        from llm_bot_helper import LLMBotPersona, get_response_for_page
        print("✓ LLM bot helper loaded")
        return True
    except Exception as e:
        print(f"✗ Failed to load LLM bot helper: {e}")
        return False


def create_llm_test_wrapper(original_bot_class, app_name):
    """
    Wrap an existing Bot class to use LLM responses

    This is a runtime wrapper that intercepts bot responses and replaces them
    with LLM-generated ones.
    """
    from llm_bot_helper import LLMBotPersona, get_response_for_page

    class LLMBotWrapper(original_bot_class):
        def play_round(self):
            # Initialize persona
            persona_id = hash(str(self.participant.id_in_session)) % 5
            persona = LLMBotPersona(persona_id)
            model = os.environ.get('OLLAMA_MODEL', 'llama3.2')

            print(f"[Bot {self.participant.id_in_session}] Using persona: {persona.name}")

            # Call original play_round but intercept yields
            for page, fields_dict in super().play_round():
                print(f"[Bot {self.participant.id_in_session}] Processing page: {page.__name__}")

                # Get page name
                page_name = page.__name__

                # Get field names
                field_names = list(fields_dict.keys())

                # Generate LLM responses
                llm_responses = get_response_for_page(
                    page_name=page_name,
                    fields=field_names,
                    app_name=app_name,
                    persona=persona,
                    model=model,
                    lang='english'
                )

                print(f"[Bot {self.participant.id_in_session}] Generated responses: {llm_responses}")

                yield page, llm_responses

    return LLMBotWrapper


def main() -> int:
    """Main execution"""

    # Handle command-line arguments
    if '--check' in sys.argv:
        return 0 if check_ollama() else 1

    if '--help' in sys.argv or '-h' in sys.argv:
        print(__doc__)
        return 0

    # Parse arguments
    num_participants = 3  # Default
    verbose = True  # Show LLM generation details by default

    for arg in sys.argv[1:]:
        if arg.isdigit():
            num_participants = int(arg)
        elif arg == '--quiet' or arg == '-q':
            verbose = False

    # Set environment variables for LLM mode
    os.environ['USE_LLM_BOTS'] = '1'  # Enable LLM mode
    if verbose:
        os.environ['LLM_BOT_VERBOSE'] = '1'

    # Check Ollama first
    if not check_ollama():
        print("\n⚠ Ollama not properly set up. Please fix the issues above.")
        return 1

    if not setup_llm_tests():
        print("\n⚠ Failed to set up LLM tests.")
        return 1

    print(f"\n{'='*60}")
    print(f"Starting LLM-powered bot test with {num_participants} participants")
    print(f"Model: {os.environ.get('OLLAMA_MODEL', 'llama3.2')}")
    print(f"Verbose mode: {'ON' if verbose else 'OFF'}")
    print(f"{'='*60}\n")

    export_path = "data/bot_test_results_llm"
    db_path = "db.sqlite3"

    # Temporarily move db
    if os.path.exists(db_path):
        os.rename(db_path, db_path + ".tmp")

    # otree imports must occur after moving db.sqlite3
    import otree.export

    try:
        from otree.bots.runner import run_all_bots_for_session_config
        from otree.main import setup

        # Setup environment
        os.environ["OTREE_IN_MEMORY"] = "1"
        setup()

        print(f"Running bot test for session config: SS_WS2526")
        print(f"Participants: {num_participants}")
        print(f"Export path: {export_path}")

        # Confirm LLM mode is enabled
        print(f"\nEnvironment check:")
        print(f"  USE_LLM_BOTS = {os.environ.get('USE_LLM_BOTS', 'not set')}")
        print(f"  LLM_BOT_VERBOSE = {os.environ.get('LLM_BOT_VERBOSE', 'not set')}")

        print("\n⏳ This will take a while with LLM responses...")
        print("   (Approximately 1-5 seconds per question per participant)\n")

        run_all_bots_for_session_config(
            session_config_name='SS_WS2526',
            num_participants=num_participants,
            export_path=export_path,
        )

        # Custom exports
        from pathlib import Path
        os.makedirs(export_path, exist_ok=True)

        apps = ['app_start', 'app_demographic', 'app_network', 'app_studium',
                'app_migration', 'app_political', 'app_end']

        for app in apps:
            try:
                fpath = Path(export_path, f"{app}_custom.csv")
                with fpath.open("w", newline="", encoding="utf8") as fp:
                    otree.export.custom_export_app(app, fp)
                print(f"✓ Exported {app}")
            except Exception as e:
                print(f"✗ Could not export {app}: {e}")

        print(f"\n{'='*60}")
        print("✓ LLM bot test completed successfully!")
        print(f"Results exported to: {export_path}/")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\n✗ Error during bot test: {e}")
        import traceback
        traceback.print_exc()
        return 1

    finally:
        # Restore original db
        if os.path.exists(db_path + ".tmp"):
            if os.path.exists(db_path):
                os.remove(db_path)
            os.rename(db_path + ".tmp", db_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
