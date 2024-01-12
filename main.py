from game import GameOfLife
from grid import Grid
from creature import ALL_CREATURES
from config import (
    dimensions,
    creature_placement_data,
    nb_generations,
    sleep_time_msec,
)


def main():
    grid = Grid(dimensions=dimensions)

    for creature_name, position in creature_placement_data:
        grid.place_creature(ALL_CREATURES[creature_name], at_position=position)

    game = GameOfLife(grid)

    game.run(nb_generations=nb_generations, sleep_time_msec=sleep_time_msec)


if __name__ == "__main__":
    main()
