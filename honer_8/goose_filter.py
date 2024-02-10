geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(arrey: list) -> list:
    return [el for el in arrey if el not in geese]
