n=int(input())
l=list(map(int,input().split()))
v=[]
for i in range(0,n-1,2):
    for j in range(l[i]):
        v.append(l[i+1])
print(*v)