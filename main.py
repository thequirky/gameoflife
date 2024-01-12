import time
from grid import Grid

from rules import get_rules_result


class GameOfLife:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    def update_grid(self) -> None:
        new_grid = self.grid.empty_grid()

        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell = self.grid.get_cell(row, col)
                nb_neighbours = self.grid.get_nb_neighbours(row, col)
                new_grid[row][col] = get_rules_result(cell, nb_neighbours)

        self.grid.grid = new_grid

    def run(self, nb_generations: int, sleep_time_msec: int) -> None:
        for generation in range(1, nb_generations + 1):
            self.update_grid()
            print(f"Generation {generation}:\n")
            print(self.grid)
            time.sleep(sleep_time_msec / 1000)


def main():
    from creatures import ALL_CREATURES

    dimensions = (20, 20)
    nb_generations = 100
    sleep_time_msec = 100
    creature_placements = [("A", (0, 0)), ("D", (10, 10))]

    grid = Grid(dimensions)

    for creature_name, position in creature_placements:
        grid.place_creature(ALL_CREATURES[creature_name], at_position=position)

    game = GameOfLife(grid)

    game.run(nb_generations=nb_generations, sleep_time_msec=sleep_time_msec)


if __name__ == "__main__":
    main()
