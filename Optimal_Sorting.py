tc=int(input())
for i in range(1,tc+1):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    if(l==s):
        print(0)
    else:
        l.sort()
        y=l.pop()
        a=l.pop(0)
        print(y-a)