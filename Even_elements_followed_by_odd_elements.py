n=int(input())
a=list(map(int,input().split()))
el=[]
ol=[]
for i in a:
    if(i%2==0):
        el.append(i)
    else:
        ol.append(i)
print(*el,*ol)
        