def title_case(titel: str, minor_words: str = '') -> str:
    titel = titel.capitalize().split()
    minor_words = minor_words.split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in titel])

minor_words = 'the of an'
string = 'a chash of kings'
# print(string.split())
result = title_case(titel=string, minor_words=minor_words)
print(result)
