from src.config.database import start_engine
from src.adapters import repository
from src.core.random_selector import RandomSelector

# TODO: Make a more clear main
def main() -> None:
    # TODO: Unit tests
    # TODO: Integration tests
    start_engine()
    repository.fill_code_challenges_table()
    save_previous_progress()



    option = input("1 if Daily practice?\n2 if add new challenge?\n")
    if option == "1":
        daily_practice()
    if option == "2":
        add_new_challenge()

def daily_practice():
    option = int(input("1 if you want to choose a random challenge\n2 if you want to choose a specific challenge\n"))
    if option == 1:
        choose_random()
    elif option == 2:
        choose_from_list()

def add_new_challenge():
    exercise_name = input("Enter the name of the exercise\n")
    exercise_description = input("Enter the description of the exercise\n")
    repository.insert_code_challenges(exercise_name, exercise_description)

# TODO: Consider a class to handle the progress
def save_previous_progress() -> None:
    challenges_tracker_id = repository.get_latest_challenges_tracker_id()

    if challenges_tracker_id:
        option = input("Did you finish the last challenge?y/n\n").strip()
        is_done = 1 if option == "y" else 0
        repository.update_challenges_tracker(challenges_tracker_id, is_done)

# TODO: remove all logic from here.
# TODO:add list curren exercices
# TODO: Consider a class to handle the random selection
def choose_random() -> None:
    random_choices = RandomSelector()
    exercise_tbd = random_choices.random_exercise
    language_tbd = random_choices.random_language

    option = input(
        "Do you want to save the progress from last the execution??y/n\n"
    ).strip()

    # TODO: Logs instead or even check if python has a better solutions for this create a module inside config and also specifc for more granular msgs
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


def choose_from_list() -> None:
    code_list = repository.get_available_code_challenges()
    exercices = {}
    languages = {
        0: "golang",
        1: "lualang",
        2: "elixirlang",
        3: "rustlang",
    }
    for i, exercice_tbd in enumerate(code_list):
        print(f"""
            Exercise ID: {i}
            Exercise Name: {exercice_tbd.exercise_name}
            Exercise Description: {exercice_tbd.exercise_description}
        """)
        exercices[i] = exercice_tbd


    for key, language in languages.items():
        print(f"{key} - {language}") 
    
    exercise_id = int(input("Choose the exercise ID you want to do\n"))
    language = int(input("Choose the language you want to do\n"))

    exercise_tbd = exercices[exercise_id]
    language_tbd = languages[language]
    
    repository.update_code_challenges(language_tbd, exercise_tbd)
    repository.insert_challenges_tracker(exercise_tbd._id, language_tbd)
        


        # print("languages available:")
        # if exercices.golang:
        #     print("golang")
        # Languages: {"golang", "rustlang", "lualang",}



if __name__ == "__main__":
    main()
