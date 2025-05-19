import random
from src.adapters import repository
from src.adapters.models import CodeChallenges


class RandomSelector:
    # TODO: Consider refactor this class
    def __init__(self):
        self.challenges = repository.get_available_code_challenges()

    @property
    def random_exercise(self) -> CodeChallenges:
        return self.challenges[random.randint(0, len(self.challenges) - 1)]

    @property
    def random_language(self) -> str:
        available_languages = [
            value.get("language")
            for value in list(
                filter(
                    lambda x: not x["bool"],
                    [
                        {"language": "golang", "bool": self.random_exercise.golang},
                        {"language": "rustlang", "bool": self.random_exercise.rustlang},
                        {"language": "lualang", "bool": self.random_exercise.lualang},
                        {
                            "language": "elixirlang",
                            "bool": self.random_exercise.elixirlang,
                        },
                    ],
                )
            )
        ]
        return random.choice(available_languages)

