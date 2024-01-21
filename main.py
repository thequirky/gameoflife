from game import GameOfLife
from grid import Grid
from creature import ALL_CREATURES
from config import config


def main():
    grid = Grid(
        dimensions=config.dimensions, infinite_boundary=config.infinite_boundary
    )

    for creature_name, position in config.creature_placement_data:
        grid.place_creature(ALL_CREATURES[creature_name], at_position=position)

    game = GameOfLife(grid)

    game.run(
        nb_generations=config.nb_generations, sleep_time_msec=config.sleep_time_msec
    )


if __name__ == "__main__":
    main()
