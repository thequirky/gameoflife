import time
from grid import Grid

from rules import ALL_RULES


class GameOfLife:
    def __init__(self, grid: Grid):
        self.grid = grid

    @staticmethod
    def get_rules_result(cell: int, nb_neighbours: int) -> None | int:
        for rule in ALL_RULES:
            result = rule(cell, nb_neighbours)
            if result is not None:
                return result

    def update_grid(self):
        new_grid = self.grid.empty_grid()

        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell = self.grid.get_cell(row, col)
                nb_neighbours = self.grid.get_nb_neighbours(row, col)
                new_cell = self.get_rules_result(cell, nb_neighbours)

                new_grid[row][col] = new_cell if new_cell is not None else cell

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

    grid = Grid(dimensions=dimensions, infinite_boundary=False)

    game = GameOfLife(grid=grid)

    for name, position in creature_placements:
        game.grid.place_creature(ALL_CREATURES[name], at_position=position)

    game.run(nb_generations=nb_generations, sleep_time_msec=sleep_time_msec)


if __name__ == "__main__":
    main()
