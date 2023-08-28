n=int(input())
l=list(map(int,input().split()))
g=int(input())
m=max(l)
v=[]
s=0
for i in l:
    s=g+i

    if(s==m or s>m):
        v.append('True')
    else:
        v.append('False')
print(*v)
