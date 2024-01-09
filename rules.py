def birth(cell: int, neighbours: int) -> int:
    if cell == 0 and neighbours == 3:
        return 1


def lonely_death(cell: int, neighbours: int) -> int:
    if cell == 1 and neighbours < 2:
        return 0


def stay_alive(cell: int, neighbours: int) -> int:
    if cell == 1 and 2 <= neighbours <= 3:
        return 1


def overpopulate(cell: int, neighbours: int) -> int:
    if cell == 1 and neighbours > 3:
        return 0


ALL_RULES = [birth, lonely_death, stay_alive, overpopulate]
