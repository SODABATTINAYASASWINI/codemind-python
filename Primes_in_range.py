def prime(n):
    if(n<=1):
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i == 0):
                return False
        return True
n=int(input())
m=int(input())
v=[]
for i in range(n,m+1):
    res = prime(i)
    if(res == True):
        v.append(i)
print(len(v))