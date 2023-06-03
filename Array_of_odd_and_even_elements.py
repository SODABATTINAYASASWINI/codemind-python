n=int(input())
a=list(map(int,input().split()))
oc=[]
ec=[]
for i in a:
    if(i%2!=0):
        oc.append(i)
    else:
        ec.append(i)
print(*oc,*ec)