# 최소, 최대
n = int(input())
k = list(map(int,input().split()))
num = []
for j in k:
    num.append(j)
num.sort()
m = num[0]
Max = num[-1]
print(m,Max,end=' ')