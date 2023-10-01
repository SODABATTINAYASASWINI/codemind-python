n=int(input())
l=list(map(int,input().split()))
v=[]
for i in l:
    if i not in v:
        v.append(i)
print(*v)