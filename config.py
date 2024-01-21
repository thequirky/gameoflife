from dataclasses import dataclass

position = tuple[int, int]
creature = str


@dataclass
class Config:
    dimensions: tuple[int, int]
    nb_generations: int
    sleep_time_msec: int
    creature_placement_data: list[tuple[creature, position]]
    infinite_boundary: bool


config = Config(
    dimensions=(20, 20),
    nb_generations=300,
    sleep_time_msec=50,
    creature_placement_data=[
        ("glider", (0, 0)),
        ("glider", (10, 0)),
        ("q_creature", (10, 10)),
    ],
    infinite_boundary=False,
)
