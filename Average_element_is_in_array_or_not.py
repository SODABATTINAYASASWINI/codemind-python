n=int(input())
a=list(map(int,input().split()))
c=0
s=sum(a)
l=len(a)
avg=s//l
if(avg in a):
    print(True)
else:
    print(False)