def longest_consec(arr: list, num: int) -> str:
    n = len(arr)
    if n == 0 or num > n or num <= 0:
        return ''
    result = ''
    for i in range(len(arr)):
        word = ''.join(arr[i:i+num])
        if len(word) > len(result):
            result = word
    return result



x = ["zone", "abigail", "theta", "form", "libe", "zas"]
print(longest_consec(arr=x, num=2))
