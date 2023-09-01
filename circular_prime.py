def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 2
n=int(input())
p=n
r=0
while(n!=0):
    t=n%10
    r=r*10+t
    n=n//10
res=prime(r)
res1=prime(p)
if(res1==1 and res==1):
    print('circular prime')
if(res!=1 and res1==1):
    print('prime but not a circular prime')
if(res!=1 and res1!=1):
    print('not prime')
    