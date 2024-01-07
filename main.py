import time

from rules import rules


class Grid:
    def __init__(self, dimensions: tuple[int, int]):
        self.rows = dimensions[0]
        self.cols = dimensions[1]
        self.grid = self.empty_grid()

    def empty_grid(self):
        return [[0] * self.cols for _ in range(self.rows)]

    def is_cell_in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_alive(self, row: int, col: int) -> bool:
        if not self.is_cell_in_bounds(row, col):
            return False
        return self.grid[row][col]

    def place_cell(self, row: int, col: int) -> None:
        self.grid[row][col] = 1

    def place_creature(self, coords: tuple[int, int]) -> None:
        for x, y in coords:
            self.place_cell(x, y)

    def alive_neighbors(self, row: int, col: int):
        positions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        return sum(
            [self.is_alive(row + off_y, col + off_x) for off_y, off_x in positions]
        )

    def __str__(self) -> str:
        rows = [" ".join(map(str, row)) for row in self.grid]
        return "\n".join(rows)


class GameOfLife:
    def __init__(self, dimensions: tuple[int, int], rules=None):
        self.grid = Grid(dimensions)
        self.rules = rules if rules else []

    def update(self):
        new_grid = [[0 for _ in range(self.grid.cols)] for _ in range(self.grid.rows)]
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell = self.grid.grid[row][col]
                alive_neighbors = self.grid.alive_neighbors(row, col)

                new_cell = None
                for rule in self.rules:
                    result = rule(cell, alive_neighbors)
                    if result is not None:
                        new_cell = result
                        break

                new_grid[row][col] = new_cell if new_cell is not None else cell

        self.grid.grid = new_grid

    def run(self, nb_generations: int, sleep_time_sec: float) -> None:
        for generation in range(1, nb_generations + 1):
            self.update()
            print(f"Generation {generation}:\n")
            print(self.grid)
            time.sleep(sleep_time_sec)


def main():
    from creatures import creatures

    dimensions = (20, 20)
    nb_generations = 60
    sleep_time_sec = 0.1

    game = GameOfLife(dimensions=dimensions, rules=rules)

    creature = creatures["default"]
    game.grid.place_creature(creature)

    game.run(nb_generations=nb_generations, sleep_time_sec=sleep_time_sec)


if __name__ == "__main__":
    main()
