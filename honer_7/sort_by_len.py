x = ["Telescopes", "Glasses", "Eyes", "Monocles"]


def sort_by_length(arrey: any) -> list:
    return sorted(arrey, key=len)


result = sort_by_length(arrey=x)
print(result)