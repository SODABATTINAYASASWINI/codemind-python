def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if(c==2):
        return -1
    else:
        return 1
m=int(input())
l=list(map(int,input().split()))
v=[]
for i in l:
    res= prime(i)
    if(res==-1):
        v.append(i)
r=sum(v)/len(v)
print("%.2f"%r)