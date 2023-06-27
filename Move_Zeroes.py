n=int(input())
a=list(map(int,input().split()))
v=[]
l=[]
for i in a:
    if(i==0):
        v.append(i)
for i in a:
    if i not in v:
        l.append(i)
print(*l,*v)
