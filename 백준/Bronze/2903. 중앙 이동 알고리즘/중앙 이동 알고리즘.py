# 중앙 이동 알고리즘
n = int(input())
first = 2
for i in range(1,n+1):
    plus = 2**(i-1)
    first += plus
print(first**2)