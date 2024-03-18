# 1,2,3 더하기
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    ans = 0
    num = [1,1,2]
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        for i in range(n-2):
            ans = num[-1]+num[-2]+num[-3]
            num.append(ans)
        print(num[-1])