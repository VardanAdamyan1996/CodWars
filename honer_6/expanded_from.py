x = 4323


def expanded_from(num: int) -> str:
    num = str(num)
    return " + ".join([num[i] + '0' * (len(num) - i - 1) for i in range(len(num))])



print(expanded_from(num=x))
