n=int(input())
a=list(map(int,input().split()))
l=len(a)
s=sum(a)
p=[]
avg=(s//l)
for i in a:
    if(i>=avg):
        p.append(i)
print(len(p))
        