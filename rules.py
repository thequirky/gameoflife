def birth(cell, neighbors):
    if cell == 0 and neighbors == 3:
        return 1
    return None


def lonely_death(cell, neighbors):
    if cell == 1 and neighbors < 2:
        return 0
    return None


def stay_alive(cell, neighbors):
    if cell == 1 and 2 <= neighbors <= 3:
        return 1
    return None


def overpopulate(cell, neighbors):
    if cell == 1 and neighbors > 3:
        return 0
    return None


rules = [birth, lonely_death, stay_alive, overpopulate]
