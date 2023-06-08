n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
s=0
for i in range(n):
    if(b[i]==1):
        s=s+(2**i)
print(s)
        