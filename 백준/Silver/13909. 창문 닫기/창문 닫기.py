# 창문 닫기

import sys
input = sys.stdin.readline
n = int(input())
i =1
cnt = 0
while i*i<=n:
    cnt+=1
    i+=1
print(cnt)