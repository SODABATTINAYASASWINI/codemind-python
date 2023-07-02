tc=int(input())
for i in range(1,tc+1):
    n=input()
    v='123456789'
    c=0
    for i in n:
        if i in v:
            c+=1
    if(c>=1):
        print('Yes')
    else:
        print('No')