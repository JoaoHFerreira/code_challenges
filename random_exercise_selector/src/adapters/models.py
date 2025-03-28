from dataclasses import dataclass, field


@dataclass
class CodeChallenges:
    _id: int
    exercise_name: str
    exercise_description: str
    golang: bool = field(default=False)
    lualang: bool = field(default=False)
    elixirlang: bool = field(default=False)
    rustlang: bool = field(default=False)

    def __post_init__(self):
        self.golang = bool(self.golang)
        self.lualang = bool(self.lualang)
        self.elixirlang = bool(self.elixirlang)
        self.rustlang = bool(self.rustlang)
