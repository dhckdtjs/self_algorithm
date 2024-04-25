# 다리 놓기
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().strip().split())
    tempx = 1
    tempy = 1
    for x in range(m,m-n,-1):
        tempx*=x
    for y in range(1,n+1):
        tempy*=y
    print(tempx//tempy)
