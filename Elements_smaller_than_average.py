n=int(input())
a=list(map(int,input().split()))
p=[]
s=sum(a)
l=len(a)
avg=s//l
for i in a:
    if(avg>=i):
        p.append(i)
print(len(p))