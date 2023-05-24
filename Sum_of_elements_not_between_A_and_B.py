n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
ls=[]
sum=0
for i in range(a,b+1):
    ls.append(i)
for i in l:
    if(i not in ls):
        sum=sum+i
print(sum)