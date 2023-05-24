n=int(input())
a=list(map(int,input().split()))
b=a[:n//2]
c=a[n//2:]
sb=sum(b)
sc=sum(c)
d=abs(sb-sc)
print(d)