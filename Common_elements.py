n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
v=[]
for i in a:
   if i in b and i not in v:
       v.append(i)
print(*v)

