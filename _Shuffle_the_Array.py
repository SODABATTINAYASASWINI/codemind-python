n=int(input())
l=list(map(int,input().split()))
s=int(input())
h1=l[:s]
h2=l[s:]
c=[]
for i in range(s):
    c.append(h1[i])
    c.append(h2[i])
print(*c)


    