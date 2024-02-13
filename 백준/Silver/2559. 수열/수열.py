# 수열
import sys
input = sys.stdin.readline
N, K = map(int,input().rstrip('\n').split())
temp_list = list(map(int,input().rstrip('\n').split()))
Sum = 0
for k in range(K):
    Sum+=temp_list[k]
Max_Sum = Sum
for i in range(N-K):
    Sum= Sum-temp_list[i]+temp_list[i+K]
    if Max_Sum<Sum:
        Max_Sum= Sum
print(Max_Sum)
