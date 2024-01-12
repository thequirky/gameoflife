from creature import Creature


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
    def __init__(self, dimensions: tuple[int, int], infinite_boundary: bool = False):
        self.rows = dimensions[0]
        self.cols = dimensions[1]
        self.infinite_boundary = infinite_boundary
        self.grid = self.empty_grid()

    def empty_grid(self) -> list[list[int]]:
        return [[0] * self.cols for _ in range(self.rows)]

    def get_cell(self, row: int, col: int) -> int:
        if self.infinite_boundary:
            row = row % self.rows
            col = col % self.cols
        return self.grid[row][col]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_alive(self, row: int, col: int) -> bool:
        return self.get_cell(row, col) == 1

    def place_cell(self, row: int, col: int) -> None:
        if self.infinite_boundary:
            row = row % self.rows
            col = col % self.cols
        self.grid[row][col] = 1

    def place_creature(self, creature: Creature, at_position: tuple[int, int]) -> None:
        for row, col in creature.coords:
            self.place_cell(row + at_position[0], col + at_position[1])

    def get_nb_neighbours(self, row: int, col: int) -> int:
        if self.infinite_boundary:
            return sum(
                [
                    self.is_alive(row + row_offset, col + col_offset)
                    for row_offset, col_offset in NEIGHBOUR_POSITIONS
                ]
            )
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
