def factors(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f
    
n=input()
l=list(n)
v=[]
for i in l:
    res=factors(int(i))
    v.append(res)
if(sum(v)==int(n)):
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')
    
    

