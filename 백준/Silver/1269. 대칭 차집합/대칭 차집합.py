# 대칭 차집합
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
A = set(map(int,input().strip().split()))
B = set(map(int,input().strip().split()))
total = A&B
res1 = A-total
res2 = B-total
print(len(res1)+len(res2))