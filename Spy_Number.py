n=int(input())
s=0
p=1
while(n!=0):
    t=n%10
    s=s+t
    p=p*t
    n=n//10
if(s==p):
    print('Spy Number')
else:
    print('Not Spy Number')