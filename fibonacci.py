n=int(input())
a=1
b=0
c=0
for i in range(n):
    print(c,end=' ')
    c=a+b
    a=b
    b=c
    