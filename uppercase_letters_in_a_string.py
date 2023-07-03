n=input()
u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=0
for i in n:
    if i in u:
        c+=1
print(c)