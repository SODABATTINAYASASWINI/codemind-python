n=int(input())
ls=list(map(int,input().split()))
sum=0
for i in ls:
    if(i%2!=0):
        sum=sum+i
print(sum)