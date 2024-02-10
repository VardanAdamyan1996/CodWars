def accum(string: str) -> str:
    return '-'.join([el.upper() + el.lower() * i for i, el in enumerate(string)])


result = accum(string='hello')
print(result)
