n=input()
v='abcdefghijklmnopqrstuvwxyz'
c=0
for i in n:
    if i in v:
        c+=1
print(c)