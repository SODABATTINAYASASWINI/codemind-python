n=int(input())
l=list(map(int,input().split()))
a=sorted(l)
j=a[::-1]
if(j==l):
    print('yes')
else:
    print('no')