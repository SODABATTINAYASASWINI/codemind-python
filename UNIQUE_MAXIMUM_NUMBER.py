n=int(input())
l=list(map(int,input().split()))
v=[]
g=[]
for i in l:
    c=l.count(i)
    if(c>1):
        v.append(i)
for i in l:
    if i not in v:
        g.append(i)
if(len(g)==0):
    print(-1)
else:
    print(max(g))