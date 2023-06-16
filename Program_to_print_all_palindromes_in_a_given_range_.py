def palen(n):
    p=n
    r=0
    while(n!=0):
        t=n%10
        r=r*10+t
        n=n//10
    if r==p:
        return 1
    else:
        return -1
n=int(input())
m=int(input())
for i in range(n,m+1):
    res=palen(i)
    if res==1:
        print(i,end=" ")
    