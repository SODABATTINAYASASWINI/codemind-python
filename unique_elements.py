n=int(input())
l=list(map(int,input().split()))
ls=[]
for i in l:
   if i not in ls:
       ls.append(i)
print(*ls)