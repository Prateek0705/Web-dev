def lar(n):
    if len(n)<=3:
        return 0
    even=n[0::2]
    odd=n[1::2]
    even.sort()
    odd.sort()
    a=even[-2]
    b=odd[1]
    return a+b
b=int(input(""))
n=[]
for i in range(b):
    e=int(input(""))
    n.append(e)    
a=lar(n)
print(a)