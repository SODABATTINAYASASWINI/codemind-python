n=int(input())
l=list(map(int,input().split()))
p=[]
c=0
for i in l:
    t=len(str(i))
    p.append(t)
for i in p:
    if(i%2==0):
        c+=1
print(c)