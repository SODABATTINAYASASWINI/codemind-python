n=int(input())
a=list(map(int,input().split()))
o=[]
e=[]
for i in a:
    if(i%2!=0):
        o.append(i)
    else:
        e.append(i)
print(*o,*e)