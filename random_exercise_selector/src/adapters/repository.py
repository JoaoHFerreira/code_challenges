from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from src.config.database import get_engine


def fill_code_challenges_table():
    # TODO: Refactor repository to be table oriented and not depeding exlusively on function name
    try:
        if is_code_challenges_filled():
            return

        with open("./data/insert.sql", "r") as file:
            sql_script = file.read()

        engine = get_engine()

        with engine.begin() as connection:
            statements = sql_script.split(";")

            for statement in statements:
                statement = statement.strip()
                if statement:
                    connection.execute(text(statement))

        print("Table filled successfully.")

    except FileNotFoundError:
        print("SQL script file not found. Check the path ./data/insert.sql")
    except SQLAlchemyError as e:
        print(f"Database error occurred: {e}")
        print("Ensure tables are created before filling. Run generate_table first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def is_code_challenges_filled():
    engine = get_engine()
    with engine.connect() as connection:
        result = connection.execute(text("SELECT _id FROM code_challenges LIMIT 1"))
        first_row = result.fetchone()

    return bool(first_row)


def get_all_available_code_challenges():
    engine = get_engine()
    with engine.connect() as connection:
        # TODO: Write queries using internals sqlalchemy
        result = connection.execute(
            text("""
            SELECT
                *
            FROM code_challenges
            WHERE
                golang = 0
                OR lualang = 0
                OR elixirlang = 0
                OR rustlang = 0
        """)
        )
        rows = result.fetchall()
    return rows


def update_code_challenges(language_tbd, exercise_tbd):
    engine = get_engine()

    with engine.connect() as connection:
        connection.execute(
            text(f"""
                UPDATE code_challenges
                SET {language_tbd} = 1
                WHERE _id = {exercise_tbd._id}
            """)
        )
        connection.commit()


def insert_challenges_tracker(code_challenge_id, language):
    engine = get_engine()
    with engine.connect() as connection:
        # TODO: Write queries using internals sqlalchemy
        connection.execute(
            text(f"""
            INSERT INTO challenges_tracker(code_challenge_id, language)
            VALUES
            ({code_challenge_id}, '{language}');
        """)
        )
        connection.commit()


def get_latest_challenges_tracker_id():
    engine = get_engine()
    with engine.connect() as connection:
        # TODO: Write queries using internals sqlalchemy
        result = connection.execute(text("select max(_id) from challenges_tracker"))
        last_id = result.fetchone()[0]
    print(last_id)
    return last_id


def update_challenges_tracker(challenges_tracker_id, is_done):
    engine = get_engine()
    with engine.connect() as connection:
        connection.execute(
            text(f"""
                UPDATE challenges_tracker
                SET 
                    end_date = CURRENT_TIMESTAMP,
                    is_done = {is_done}
                WHERE _id = {challenges_tracker_id}
            """)
        )
        connection.commit()
