n=input()
v='123456789'
l=[]
for i in n:
    if i in v:
        s=int(i)
        l.append(s)
        
print(sum(l))

        
    