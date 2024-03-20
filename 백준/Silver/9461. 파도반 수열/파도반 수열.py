# 파도반 수열
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1,T+1):
    num = [0, 1, 1, 1, 2]
    n = int(input())
    if n<5:
        print(num[n])
    else:
        for i in range(n-4):
            k = num[-1]+num[i]
            num.append(k)
        # print(num)
        print(num[-1])
