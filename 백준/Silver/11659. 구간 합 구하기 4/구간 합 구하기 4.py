# 구간 합 구하기 4
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().rstrip().split()))
sum_list = [0]
sm = 0
for i in range(len(num)):
    sm +=num[i]
    sum_list.append(sm)
for _ in range(M):
    start,end = map(int,input().split())
    print(sum_list[end]-sum_list[start-1])