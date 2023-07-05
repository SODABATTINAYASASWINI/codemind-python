import statistics
n=int(input())
l=list(map(int,input().split()))
res=statistics.mode(l)
print(res)