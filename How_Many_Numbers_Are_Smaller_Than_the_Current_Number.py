n=int(input())
a=list(map(int,input().split()))
v=[]
for i in range(n):
    c=0
    for j in range(n):
        if(j!=i):
            if(a[i]>a[j]):
                c+=1
    v.append(c)   
print(*v)