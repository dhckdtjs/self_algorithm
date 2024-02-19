# 빠른 A+B
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    A,B = map(int,input().rstrip('\n').split())
    print(A+B)
