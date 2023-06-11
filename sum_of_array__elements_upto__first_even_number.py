n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i%2==0:
        k=i
        break
    l.append(i)
print(sum(l))
