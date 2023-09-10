n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
v=[]
for i in range(n):
    if(l[i]<a or l[i]>b):
        v.append(l[i])
if(len(v)==0):
    print('-1')
else:
    print(*v)
    