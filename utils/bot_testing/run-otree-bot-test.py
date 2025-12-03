import os
import sys

# The cli command `otree bots` does not allow for custom exports, thus it is
# replicated here.

def main() -> int:
    # Parse command-line arguments
    # Usage: python script.py [URL] [REST_KEY] [NUM_PARTICIPANTS]
    session_url = sys.argv[1] if len(sys.argv) > 1 else None
    rest_key = sys.argv[2] if len(sys.argv) > 2 else os.environ.get('OTREE_REST_KEY')
    num_participants = int(sys.argv[3]) if len(sys.argv) > 3 else 10  # Default to 50
    export_path = "data/bot_test_results"
    db_path = "db.sqlite3"
    # temporarily move db
    if os.path.exists(db_path):
        os.rename(db_path, db_path + ".tmp")
    # otree imports must occur after moving db.sqlite3 to successfully create a
    # new db file.
    import otree.export

    try:
        if session_url:
            # Test external session via URL using browser automation
            if not rest_key:
                print("ERROR: REST key required for testing external servers.")
                print("Provide it via:")
                print("  1. Command line: python script.py <URL> <REST_KEY>")
                print("  2. Environment variable: export OTREE_REST_KEY=your_key")
                return 1

            print(f"Running bot test for URL: {session_url}")
            print("Note: Testing external URLs requires browser automation.")
            print("This will open browser windows to test the survey.")
            print("\nIMPORTANT: Please close Chrome/Chromium before running this test.")

            # Extract server URL and session config from the room URL
            # Expected format: http://domain/room/RoomName
            from urllib.parse import urlparse
            parsed = urlparse(session_url)

            # Force HTTPS if the server is redirecting
            scheme = parsed.scheme
            if scheme == 'http':
                print("Note: Converting HTTP to HTTPS (server requires secure connection)")
                scheme = 'https'

            server_url = f"{scheme}://{parsed.netloc}"

            print(f"Server URL: {server_url}")
            print(f"Testing session config: SS_WS2526 with {num_participants} participants")

            # Use otree browser_bots command for external URLs
            import subprocess
            env = os.environ.copy()
            env['OTREE_REST_KEY'] = rest_key

            result = subprocess.run(
                ['otree', 'browser_bots', 'SS_WS2526', str(num_participants), '--server-url', server_url],
                cwd=os.path.dirname(os.path.abspath(__file__)) + '/../..',
                capture_output=True,
                text=True,
                env=env
            )

            # Print stdout and stderr for debugging
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print("STDERR:", result.stderr, file=sys.stderr)

            if result.returncode != 0:
                raise Exception(f"Bot test failed with return code {result.returncode}")
        else:
            # Test local session config
            from otree.bots.runner import run_all_bots_for_session_config
            from otree.main import setup

            # replicating behavior from otree.main.execute_from_command_line()
            os.environ["OTREE_IN_MEMORY"] = "1"
            setup()
            print(f"Running bot test for local session config: SS_WS2526 with {num_participants} participants")
            run_all_bots_for_session_config(
                session_config_name='SS_WS2526',
                num_participants=num_participants,
                export_path=export_path,
            )

        # Add custom exports if needed
        from pathlib import Path

        os.makedirs(export_path, exist_ok=True)

        # Export data for each app
        apps = ['app_start', 'app_demographic', 'app_network','app_studium', 'app_migration', 'app_political', 'app_end']
        for app in apps:
            try:
                fpath = Path(export_path, f"{app}_custom.csv")
                with fpath.open("w", newline="", encoding="utf8") as fp:
                    otree.export.custom_export_app(app, fp)
                print(f"Exported {app}")
            except Exception as e:
                print(f"Could not export {app}: {e}")

        print("\nBot test completed successfully!")
        print(f"Results exported to: {export_path}/")

    except Exception as e:
        print(f"Error during bot test: {e}")
        import traceback
        traceback.print_exc()
        return 1
    finally:
        # remove test db, restore original
        if os.path.exists(db_path + ".tmp"):
            if os.path.exists(db_path):
                os.remove(db_path)
            os.rename(db_path + ".tmp", db_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
