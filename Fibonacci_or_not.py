n=int(input())
a=0
b=1
l=[]
for i in range(1,n+1):
    c=a+b
    l.append(c)
    a=b
    b=c
if(n in l):
    print(True)
else:
    print(False)