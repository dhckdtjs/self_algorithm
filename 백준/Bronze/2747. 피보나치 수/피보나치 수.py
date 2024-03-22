# 피보나치 수
import sys
input = sys.stdin.readline
DP = [0,1]
n = int(input())
if n < 2:
    print(DP[n])
else:
    for i in range(n-1):
        num = DP[-1]+DP[-2]
        DP.append(num)
    print(DP[-1])