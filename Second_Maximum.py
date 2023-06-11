tc=int(input())
for i in range(1,tc+1):
    a=list(map(int,input().split()))
    s=sorted(a)
    w=s[-2]
    print(w)