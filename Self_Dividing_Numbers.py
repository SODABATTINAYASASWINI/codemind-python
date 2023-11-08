def divi(i):
    v=[]
    c=0
    l=list(str(i))
    for j in l:
        if(int(j)!=0 and i!=0):
            if(i%int(j)==0):
                c+=1
    if(c == len(l)):
        v.append(i)
    return v
n = int(input())
m=int(input())
res =[]
for i in range(n,m+1):
    res+=divi(i)
print(*res,sep=' ')
    
    