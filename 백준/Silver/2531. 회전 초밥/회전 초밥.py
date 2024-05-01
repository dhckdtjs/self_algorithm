n,d,k,c = map(int,input().split())
belt = []
for i in range(n):
    one = int(input())
    belt.append(one)
a = 0
b = k
max_v= -float('inf')
while a != n:
    if a<=n-k :
        temp = belt[a:b]
    else:
        temp = belt[a:n] + belt[0:b+1]
    temp = set(temp)
    temp.add(c)
    max_v = max(max_v,len(temp))
    a += 1
    b = (b+1)%(n+1)
print(max_v)