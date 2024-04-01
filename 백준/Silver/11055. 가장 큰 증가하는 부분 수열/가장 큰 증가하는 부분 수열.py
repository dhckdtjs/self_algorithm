# 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().strip().split()))
dp = [0]*n

# 각 요소에 대해 dp[i]를 num[i]로 초기화합니다.
for i in range(n):
    dp[i] = num[i]

# i번째 요소에 대해 i보다 앞에 있는 요소들 중 num[i]보다 작은 것들을 찾아
# 그 위치의 dp 값에 num[i]를 더한 값으로 dp[i]를 업데이트합니다.
for i in range(1,n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], num[i] + dp[j])

# 가장 큰 증가하는 부분 수열의 합을 출력합니다.
print(max(dp))
