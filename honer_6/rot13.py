def rot13(message: str) -> str:
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for el in message:
        if el in alpha.lower():
            result += alpha[(alpha.lower().index(el) + 13) % 26]
        elif el in alpha:
            result += alpha[(alpha.index(el) + 13) % 26]
        else:
            result += el
    return result


