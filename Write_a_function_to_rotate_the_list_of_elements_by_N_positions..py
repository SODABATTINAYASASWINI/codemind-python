n=int(input())
l=list(map(int,input().split()))
r=int(input())
for i in range(1,r+1):
    t=l.pop()
    l.insert(0,t)
print(*l)