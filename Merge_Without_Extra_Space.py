tc=int(input())
for i in range(1,tc+1):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.extend(l2)
    l1.sort()
    print(*l1)
    