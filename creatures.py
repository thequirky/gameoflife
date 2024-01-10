def to_coords(creature: list[str]) -> list[tuple[int, int]]:
    coords = []
    for row_nb, row_str in enumerate(creature):
        for col_nb, cell in enumerate(row_str):
            if cell == "1":
                coords.append((row_nb, col_nb))
    return coords


ALL_CREATURES = {
    "A": to_coords(
        [
            "010",
            "001",
            "111",
        ]
    ),
    "D": to_coords(
        [
            "0110",
            "1001",
            "1011",
            "0110",
        ]
    ),
}
