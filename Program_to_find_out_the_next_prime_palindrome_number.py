def is_prime(n):
    if(n<=1):
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
        return True
        
def palin(n):
    n=str(n)
    if(n[::-1] == n):
        return True
        
n=int(input())
nex=n+1
while(1):
    if (is_prime(nex) and palin(nex)):
        print(nex)
        break
    nex+=1
    