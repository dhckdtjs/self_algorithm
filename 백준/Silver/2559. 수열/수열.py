# 수열
# 연속되는 값 더한 값 중 최대값 구하기
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
temp_list = list(map(int,input().split()))
Sum_list = []
Sum_list.append(sum(temp_list[:K]))
for i in range(N-K):
    result = (Sum_list[i]-temp_list[i]+temp_list[i+K])
    Sum_list.append(result)
print(max(Sum_list))