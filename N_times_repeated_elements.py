n=int(input())
l=list(map(int,input().split()))
q=int(input())
v=[]
y=[]
s=set(l)
for i in s:
    c=l.count(i)
    v.append(c)
if q in v:
    for i in s:
        if l.count(i)==q:
            y.append(i)
    print(*y)
else:
    print(-1)
    