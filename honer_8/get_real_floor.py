def get_real_floor(floor: int) -> int:
    if floor > 0:
        if floor == 1:
            return floor - 1
        elif floor > 13:
            return floor - 2
        else:
            return floor - 1
    return floor
