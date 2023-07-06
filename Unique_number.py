n=int(input())
s=list(str(n))
v=[]
for i in s:
    if i in s and i not in v:
        v.append(i)
if len(v)==len(s):
    print('Unique Number')
else:
    print('Not Unique Number')