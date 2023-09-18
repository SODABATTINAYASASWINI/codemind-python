n,m=map(int,input().split())
l=list(map(int,input().split()))
v=[]
for i in range(m):
    p=l.pop(0)
    l.append(p)
print(*l)