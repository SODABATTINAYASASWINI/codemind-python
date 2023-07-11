tc=int(input())
for i in range(1,tc+1):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    for j in range(1,b+1):
        t=l.pop()
        l.insert(0,t)
    print(*l)