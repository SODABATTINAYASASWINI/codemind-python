n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
aa=set(a)
bb=set(b)
c=aa&bb
print(len(c))