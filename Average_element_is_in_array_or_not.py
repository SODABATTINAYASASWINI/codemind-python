n=int(input())
ls=list(map(int,input().split()))
s=sum(ls)
avg=s//len(ls)
if(avg in ls):
    print('True')
else:
    print('False')