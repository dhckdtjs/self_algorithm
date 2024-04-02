# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().strip().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if num[i]>num[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))