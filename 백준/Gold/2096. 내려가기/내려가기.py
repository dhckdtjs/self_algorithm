# 내려가기
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
dp = [[0]*6 for _ in range(n)]
for k in range(6):
    dp[0][k] = arr[0][k%3]
# dp[0]         # 1 2 3 1 2 3
for i in range(1,n):
    dp[i][0] = max(dp[i-1][0],dp[i-1][1])+arr[i][0]
    dp[i][1] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])+arr[i][1]
    dp[i][2] = max(dp[i-1][1],dp[i-1][2])+arr[i][2]
    dp[i][3] = min(dp[i - 1][3], dp[i - 1][4]) + arr[i][0]
    dp[i][4] = min(dp[i - 1][3], dp[i - 1][4], dp[i - 1][5]) + arr[i][1]
    dp[i][5] = min(dp[i - 1][4], dp[i - 1][5]) + arr[i][2]
# print(dp)
max_v = -float('inf')
min_v = float('inf')
for l in dp[-1][0:3]:
   if max_v<l:
       max_v = l
for h in dp[-1][3:6]:
    if min_v>h:
        min_v = h
print(max_v,min_v)