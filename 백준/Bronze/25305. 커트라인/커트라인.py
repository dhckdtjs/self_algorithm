# 커트라인
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort(reverse=True)
print(num[m-1])