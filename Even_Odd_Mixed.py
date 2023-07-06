n=int(input())
s=list(str(n))
ec=0
oc=0
c=0
while(n!=0):
    t=n%10
    if(t%2==0):
        ec+=1
    elif(t%2!=0):
        oc+=1
    else:
        c+=1
    n=n//10
if ec==len(s):
    print('Even')
elif oc==len(s):
    print('Odd')
else:
    print('Mixed')