def a12(b):
    a=int(b[0])
    i=1
    while i<len(b):
        if b[i]=='A':
            a&=int(b[i+1])
        elif b[i]=='B':
            a|=int(b[i+1])
        else:
            a^=int(b[i+1])
        i+=2
    return a
b=input()
print(a12(b))