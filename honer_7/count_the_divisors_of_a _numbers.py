def count_divisors(num: int) -> int:
    count = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            if i * i == num:
                count += 1
            else:
                count += 2
        i += 1
    return count



