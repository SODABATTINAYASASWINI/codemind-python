n=int(input())
s=list(str(n))
a=s.pop()
b=s.pop()
c=s.pop()
s.append(a)
s.append(b)
s.append(c)
y=''.join(s)
print(y)