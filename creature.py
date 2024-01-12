class Creature:
    def __init__(self, signature: list[str]) -> None:
        self.signature = signature

    @property
    def coords(self) -> list[tuple[int, int]]:
        coords = []
        for row_nb, row_str in enumerate(self.signature):
            for col_nb, cell in enumerate(row_str):
                if cell == "1":
                    coords.append((row_nb, col_nb))
        return coords


glider = Creature(
    signature=[
        "010",
        "001",
        "111",
    ]
)

q_creature = Creature(
    signature=[
        "0110",
        "1001",
        "1011",
        "0110",
    ]
)

ALL_CREATURES = {"glider": glider, "q_creature": q_creature}
