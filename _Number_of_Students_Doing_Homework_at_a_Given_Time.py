n=int(input())
s=list(map(int,input().split()))
n1=int(input())
e=list(map(int,input().split()))
q=int(input())
c=0
for i in range(n):
    if(e[i]>=q and s[i]<=q):
        c+=1
print(c)