n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
l=[]
for i in range(n2):
    l.insert(l2[i],l1[i])
print(*l)