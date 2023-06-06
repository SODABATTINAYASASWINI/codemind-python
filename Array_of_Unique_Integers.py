n=int(input())
a=list(map(int,input().split()))
mi=min(a)
ma=max(a)
avg=(mi+ma)//2
print("%.5f"%avg)