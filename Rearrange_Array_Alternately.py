tc=int(input())
for i in range(1,tc+1):
    v=[]
    p=[]
    n=int(input())
    l=list(map(int,input().split()))
    for j in range(n):
        if len(l)!=0:
            ma=max(l)
            mi=min(l)
            l.pop()
            if len(l)!=0:
                 l.pop(0)
            v.append(ma) 
            v.append(mi) 
    for k in v:
        if k not in p:
            p.append(k)
    print(*p)