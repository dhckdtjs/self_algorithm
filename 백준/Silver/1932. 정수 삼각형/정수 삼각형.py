# 정수 삼각형
import sys
input = sys.stdin.readline
n = int(input())
tri= []
dp = []
for i in range(n):
    dp_r = [0]*(i+1)
    row = list(map(int,input().strip().split()))
    tri+=[row]
    dp+=[dp_r]
r = 0
c = 0
dp[r][c] = tri[0][0]

for j in range(n-1):
    for k in range(len(tri[j])):
        temp1 = dp[j][k]+tri[j+1][k]
        temp2 = dp[j][k]+tri[j+1][k+1]
        if dp[j+1][k]<temp1:
            dp[j+1][k] = temp1
        if dp[j+1][k+1]<temp2:
            dp[j+1][k+1]=temp2
Max = -float('inf')
for lst in dp[-1]:
    if Max<lst:
        Max=lst
print(Max)