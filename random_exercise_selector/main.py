from src.config.database import start_engine
from src.adapters import repository
from src.core.random_selector import RandomSelector


def main():
    start_engine()
    repository.fill_code_challenges_table()
    save_previous_progress()
    choose_random()


def save_previous_progress():
    challenges_tracker_id = repository.get_latest_challenges_tracker_id()
    if challenges_tracker_id:
        repository.update_challenges_tracker(challenges_tracker_id)


def choose_random():
    random_choices = RandomSelector()
    exercise_tbd = random_choices.random_exercise
    language_tbd = random_choices.random_language

    print(f"""
        Exercise Name: {exercise_tbd.exercise_name}
        Exercise Description: {exercise_tbd.exercise_description}
        Language: {language_tbd}
    """)
    option = input("The suggested challenge and language are ok for you?y/n\n").strip()
    if option == "y":
        repository.update_code_challenges(language_tbd, exercise_tbd)
        repository.insert_challenges_tracker(exercise_tbd._id, language_tbd)
        print(f"""
            Exercise Name: {exercise_tbd.exercise_name}
            Exercise Description: {exercise_tbd.exercise_description}
            Language: {language_tbd}
        """)
        return
    choose_random()


if __name__ == "__main__":
    main()
