import time


NEIGHBOUR_POSITIONS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


class Grid:
    def __init__(self, dimensions: tuple[int, int], infinite: bool = False):
        self.rows = dimensions[0]
        self.cols = dimensions[1]
        self.infinite = infinite
        self.grid = self.empty_grid()

    def empty_grid(self):
        return [[0] * self.cols for _ in range(self.rows)]

    def get_cell(self, row: int, col: int) -> int:
        if self.infinite:
            row = row % self.rows
            col = col % self.cols
        return self.grid[row][col]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_alive(self, row: int, col: int) -> bool:
        return self.get_cell(row, col) == 1

    def place_cell(self, row: int, col: int) -> None:
        if self.infinite:
            row = row % self.rows
            col = col % self.cols
        self.grid[row][col] = 1

    def place_creature(
        self, coords: tuple[int, int], at_position: tuple[int, int]
    ) -> None:
        for row, col in coords:
            self.place_cell(row + at_position[0], col + at_position[1])

    def get_nb_neighbours(self, row: int, col: int):
        if self.infinite:
            return sum(
                [
                    self.is_alive(row + row_offset, col + col_offset)
                    for row_offset, col_offset in NEIGHBOUR_POSITIONS
                ]
            )
        else:
            return sum(
                [
                    self.is_alive(row + row_offset, col + col_offset)
                    for row_offset, col_offset in NEIGHBOUR_POSITIONS
                    if self.is_in_bounds(row + row_offset, col + col_offset)
                ]
            )

    def __str__(self) -> str:
        rows = [" ".join(map(str, row)) for row in self.grid]
        return "\n".join(rows)


class GameOfLife:
    def __init__(self, dimensions: tuple[int, int], rules=[]):
        self.grid = Grid(dimensions)
        self.rules = rules

    def update(self):
        new_grid = self.grid.empty_grid()

        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell = self.grid.get_cell(row, col)
                nb_neighbours = self.grid.get_nb_neighbours(row, col)

                new_cell = None
                for rule in self.rules:
                    result = rule(cell, nb_neighbours)
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
    from creatures import CREATURES
    from rules import ALL_RULES

    dimensions = (20, 20)
    nb_generations = 100
    sleep_time_sec = 0.1

    game = GameOfLife(dimensions=dimensions, rules=ALL_RULES)

    creature_placements = [
        ("default", (0,0)),
        ("mirrorred", (10,10))
    ]
    for name, position in creature_placements:
        game.grid.place_creature(CREATURES[name], at_position=position)

    game.run(nb_generations=nb_generations, sleep_time_sec=sleep_time_sec)


if __name__ == "__main__":
    main()
