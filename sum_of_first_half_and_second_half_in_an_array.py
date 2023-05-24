n=int(input())
a=list(map(int,input().split()))
b=a[:n//2]
c=a[n//2:]
print(sum(b))
print(sum(c))