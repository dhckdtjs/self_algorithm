# Four Squares
import math
n = int(input())
dp = [0,1]

for i in range(2,n+1):
    min_v =4
    for j in range(1,int(math.sqrt(i))+1):
        min_v = min(min_v,dp[i-j**2])
    dp.append(min_v+1)
print(dp[n])