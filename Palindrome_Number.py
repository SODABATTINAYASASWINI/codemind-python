t=int(input())
for i in range(1,t+1):
    n=int(input())
    r=0
    i=1
    p=n
    while n>0:
        t=n%10
        r=r*10+t
        n=n//10
        i=i+1
    if p==r:
        print('True')
    else:
        print('False')