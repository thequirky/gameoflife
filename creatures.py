def to_coords(creature: list[str]) -> list[tuple[int, int]]:
    coords = []
    for row_nb, row_str in enumerate(creature):
        for col_nb, cell in enumerate(row_str):
            print(cell, cell == "1", f" - ({row_nb},{col_nb})")
            if cell == "1":
                coords.append((row_nb, col_nb))
    return coords


A = [
    "010",
    "001",
    "111",
]

B = [
    "011",
    "101",
    "001",
]

C = [
    "010",
    "101",
    "111",
]

D = [
    "0110",
    "1001",
    "1011",
    "0110",
]


