def signature_to_coords(signature: list[str]) -> list[tuple[int, int]]:
    coords = []
    for row_nb, row_str in enumerate(signature):
        for col_nb, cell in enumerate(row_str):
            if cell == "1":
                coords.append((row_nb, col_nb))
    return coords


glider = signature_to_coords(
    [
        "010",
        "001",
        "111",
    ]
)

q_creature = signature_to_coords(
    [
        "0110",
        "1001",
        "1011",
        "0110",
    ]
)

ALL_CREATURES = {"glider": glider, "q_creature": q_creature}
