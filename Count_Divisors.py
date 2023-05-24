a,r,k=map(int,input().split())
ls=[]
for i in range(a,r+1):
    if(i%k==0):
       ls.append(i)
print(len(ls))