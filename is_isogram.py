def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))

palavra = input()
print(is_isogram(palavra))


