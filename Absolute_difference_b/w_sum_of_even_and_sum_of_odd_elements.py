n=int(input())
ls=list(map(int,input().split()))
sume=0
sumo=0
for i in ls:
    if(i%2!=0):
        sume=sume+i
    else:
        sumo=sumo+i
if(sume>sumo):
    print(sume-sumo)
else:
    print(sumo-sume)