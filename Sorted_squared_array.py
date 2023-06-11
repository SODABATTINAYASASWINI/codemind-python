n=int(input())
a=list(map(int,input().split()))
s=sorted(a)
v=[]
for i in s:
    p=i**2
    v.append(p)
print(*v)