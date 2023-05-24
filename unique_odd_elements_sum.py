n=int(input())
l=list(map(int,input().split()))
s=set(l)
sum=0
for i in s:
    if(i%2!=0):
        sum=sum+i
print(sum)