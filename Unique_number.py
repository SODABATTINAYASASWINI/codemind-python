n=input()
l=list(n)
v=[]
for i in l:
   if i in l and i not in v:
       v.append(i)
if v==l:
    print('Unique Number')
else:
    print('Not Unique Number')
