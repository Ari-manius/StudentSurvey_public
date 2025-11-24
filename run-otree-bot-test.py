import os

# The cli command `otree bots` does not allow for custom exports, thus it is
# replicated here.


def main() -> int:
    export_path = "bot_test_results"
    db_path = "db.sqlite3"
    # temporarily move db
    if os.path.exists(db_path):
        os.rename(db_path, db_path + ".tmp")
    # otree imports must occur after moving db.sqlite3 to successfully create a
    # new db file.
    import otree.export

    try:
        from otree.bots.runner import run_all_bots_for_session_config
        from otree.main import setup

        # replicating behavior from otree.main.execute_from_command_line()
        os.environ["OTREE_IN_MEMORY"] = "1"
        setup()
        run_all_bots_for_session_config(
            session_config_name='SS_WS2526',
            num_participants=10,
            export_path=export_path,
        )

        # Add custom exports if needed
        from pathlib import Path

        os.makedirs(export_path, exist_ok=True)

        # Export data for each app
        apps = ['app_start', 'app_demographic', 'app_studium', 'app_network', 'app_migration', 'app_political', 'app_end']
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
