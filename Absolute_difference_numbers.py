n,x=map(int,input().split())
v=[]
k=[]
vr=[]
g=list(str(n))
for i in range(1,x+1):
    a=g.pop()
    v.append(a)
p=g[::-1]
for i in range(1,x+1):
    b=p.pop()
    k.append(b)
vr=v[::-1]
vr= ''.join(vr)          
vr= int(vr) 
k= ''.join(k)         
k= int(k) 
if(k>vr):
    print(k-vr)
else:
    print(vr-k)



    
    