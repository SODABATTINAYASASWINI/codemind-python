n=int(input())
a=list(map(int,input().split()))
a.sort()
c=0
b=set(a)
for i in b:
    f=a.count(i)
    if f>1:
        c+=f//2
print(c)