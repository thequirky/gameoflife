def birth(cell: int, neighbours: int) -> None | int:
    if cell == 0 and neighbours == 3:
        return 1


def lonely_death(cell: int, neighbours: int) -> None | int:
    if cell == 1 and neighbours < 2:
        return 0


def stay_alive(cell: int, neighbours: int) -> None | int:
    if cell == 1 and 2 <= neighbours <= 3:
        return 1


def overpopulate(cell: int, neighbours: int) -> None | int:
    if cell == 1 and neighbours > 3:
        return 0


all_rules = [birth, lonely_death, stay_alive, overpopulate]


def evaluate_rules(cell: int, nb_neighbours: int) -> None | int:
    for rule in all_rules:
        result = rule(cell, nb_neighbours)
        if result is not None:
            return result
    return cell