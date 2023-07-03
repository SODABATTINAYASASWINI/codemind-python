n=input()
v='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
va='abcdefghijklmnopqrstuvwxyz'
s=' '
c=0
for i in n:
    if i not in v and i not in va and i not in s:
        c+=1
print(c)