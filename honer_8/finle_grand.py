def finle_grand(exem: int, project: int) -> int:
    if exem >= 90 or project >= 10:
        return 100
    elif exem >= 75 or project >= 5:
        return 90
    elif exem >= 50 or project >= 2:
        return 70
    return 0
