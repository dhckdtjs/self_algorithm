# 계단 오르기
import sys
input = sys.stdin.readline
n = int(input())
stair = [0]*(n+1)
for i in range(1,n+1):
    stair[i] = int(input())
# print(stair)
dp = [[0]*3 for _ in range(n+1)]
# print(dp)
for i in range(1,n+1):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2])
    dp[i][1] = dp[i-1][0]+stair[i]
    dp[i][2] = dp[i-1][1]+stair[i]
print(max(dp[n][1],dp[n][2]))
