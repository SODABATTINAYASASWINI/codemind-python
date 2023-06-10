n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
c=0
s=0
for i in b:
    x=i*10**c
    s=s+x
    c+=1
w=s+1
st=str(w)
print(*st)