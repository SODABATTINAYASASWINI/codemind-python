import statistics
n=int(input())
l=list(map(int,input().split()))
s=statistics.mode(l)
print(s)