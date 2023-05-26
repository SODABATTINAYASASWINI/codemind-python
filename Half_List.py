n=int(input())
l=list(map(int,input().split()))
a=l[:n//2]
b=l[n//2:]
b.reverse()
print(*b,*a)