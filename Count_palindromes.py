n=int(input())
l=list(map(int,input().split()))
r=0
c=0
for i in l:
    y=i
    while(i!=0):
        t=i%10
        r=r*10+t
        i=i//10
    if r==y:
        c+=1
    r=0
print(c)
        