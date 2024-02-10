x = [':D', ':(', ':)', ';~D', ';}', ';[']
print(len(x[0]))

def count_smileys(arr: list) -> int:
    count = 0
    eyes = [':', ';']
    noses = ['-', '~']
    mouths = ['D', ')']
    for el in arr:
        if len(el) == 2:
            if el[0] in eyes and el[1] in mouths:
                count += 1
        elif len(el) == 3:
            if el[0] in eyes and el[1] in noses and el[2] in mouths:
                count += 1
    return count


result = count_smileys(arr=x)
print(result)
