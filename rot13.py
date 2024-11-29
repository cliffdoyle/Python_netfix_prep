"""implementation of rot13 in python"""


def rot13(word, num):
    res = []
    for ch in word:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch)-ord('a')+num) % 26+ord('a')))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch)-ord('A')+num) % 26+ord('A')))
        else:
            res.append(ch)
    return ''.join(res)


print(rot13('hello', 3))
