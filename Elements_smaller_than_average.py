n=int(input())
a=list(map(int,input().split()))
l=len(a)
s=sum(a)
ls=[]
avg=s//l
for i in a:
    if(i<=avg):
        ls.append(i)
print(len(ls))