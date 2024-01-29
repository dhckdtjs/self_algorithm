n = int(input())
Lope = []
for i in range(1,n+1):
    L = int(input())
    Lope.append(L)
Lope.sort()
Max = 0
for k in range(n):
    result = Lope[k]*(n-k)
    if Max<result:
        Max=result
print(Max)