def rot2(word,n):
    res=[]
    for ch in word:
        if 'a'<=ch<='z':
            res.append(chr((ord(ch)-ord('a')+n)%26+ord('a')))
        elif 'A'<=ch<='Z':
            res.append(chr((ord(ch)-ord('a')+n)%26+ord('a')))
        else:
            res.append(ch)
            
    return ''.join(res)

print(rot2('hello',6))