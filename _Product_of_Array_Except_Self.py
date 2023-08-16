n=int(input())
l=list(map(int,input().split()))
p=1
for i in l:
    p=p*i
for i in l:
    print(p//i,end=' ')