n=int(input())
a=list(map(int,input().split()))
se=int(input())
if se not in a:
    print("-1")
else:
    print(a.index(se))