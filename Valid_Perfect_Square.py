t=int(input())
for i in range(1,t+1):
    n=int(input())
    r=n**0.5
    p=int(r)
    c=p*p
    if(c==n):
        print('True')
    else:
        print('False')
    