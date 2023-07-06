n=int(input())
o=n
p=[]
while(n>0):
    if n%2==0:
        n=n//2
    else:
       n=3*n+1
    if(n==1):
        break
    p.append(n)
print(o,*p,'1')
    