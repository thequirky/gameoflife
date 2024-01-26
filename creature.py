coord = tuple[int, int]


class Creature:
    def __init__(self, name: str, pattern: list[str]) -> None:
        self.name = name
        self.pattern = pattern

    @property
    def coords(self) -> list[coord]:
        coords = []
        for row_nb, row_str in enumerate(self.pattern):
            for col_nb, cell in enumerate(row_str):
                if cell == "1":
                    coords.append((row_nb, col_nb))
        return coords


glider = Creature(
    name="glider",
    pattern=[
        "010",
        "001",
        "111",
    ],
)

q_creature = Creature(
    name="q_creature",
    pattern=[
        "0110",
        "1001",
        "1011",
        "0110",
    ],
)

ALL_CREATURES = {"glider": glider, "q_creature": q_creature}
