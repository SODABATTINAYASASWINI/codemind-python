tc=int(input())
for k in range(1,tc+1):
    n=input()
    l=list(n)
    r=l[::-1]
    if(r==l):
        if(len(r)%2==0):
            print('YES','EVEN')
        else:
            print('YES','ODD')
    else:
        print("NO")