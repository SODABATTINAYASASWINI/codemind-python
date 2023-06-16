n=int(input())
l=list(map(int,input().split()))
r=0
rs=[]
c=0
for i in l:
    while(i!=0):
        t=i%10
        r=r*10+t
        i=i//10
    rs.append(r)
    r=0
    
print(*rs)
        