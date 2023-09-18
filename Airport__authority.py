n=int(input())
v=[]
c=0
for i in range(1,n+1):
    v.append(int(input()))
t=int(input())
for i in v:
    if(i<=t):
        c+=1
    else:
        c+=2
print(c)
        

    