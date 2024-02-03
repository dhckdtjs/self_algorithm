# 제로 
# K input으로 받음
# 0 받으면 가장 최근 숫자 지움
# 최종적으로 합 output
from collections import deque
K = int(input())
Zero = deque()
for _ in range(K):
    num = int(input())
    if num == 0:
        Zero.pop()
    else:
        Zero.append(num)
Sum = 0
for i in Zero:
    Sum+=i
print(Sum)