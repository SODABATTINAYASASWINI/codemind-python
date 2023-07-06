tc=int(input())
for j in range(1,tc+1):
    n=int(input())
    l=list(map(int,input().split()))
    v=[]
    for i in range(1,n+1):
       if i not in l:
          v.append(i)
    print(*v)