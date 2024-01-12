import time
from grid import Grid

from rules import evaluate_rules


class GameOfLife:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    def update_grid(self) -> None:
        new_grid = self.grid.empty_grid()

        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell = self.grid.get_cell(row, col)
                nb_neighbours = self.grid.get_nb_neighbours(row, col)
                new_grid[row][col] = evaluate_rules(cell, nb_neighbours)

        self.grid.grid = new_grid

    def run(self, nb_generations: int, sleep_time_msec: int) -> None:
        for generation in range(1, nb_generations + 1):
            self.update_grid()
            print(f"Generation {generation}:\n")
            print(self.grid)
            time.sleep(sleep_time_msec / 1000)