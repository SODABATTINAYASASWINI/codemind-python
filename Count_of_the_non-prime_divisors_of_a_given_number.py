def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
v=[]
p=[]
r=[]
for i in range(1,n+1):
    if n%i==0:
       v.append(i)
for i in v:
    res=prime(i)
    if(res==1):
        p.append(i)
for i in v:
    if i not in p:
        r.append(i)
print(len(r))
    
    