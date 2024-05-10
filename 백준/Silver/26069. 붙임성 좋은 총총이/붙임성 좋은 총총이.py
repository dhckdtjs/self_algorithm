# 붙임성 좋은 총총이
import sys
input = sys.stdin.readline
n = int(input())
chong = set()
chong.add('ChongChong')
for i in range(n):
    a,b = input().split()
    if a in chong:
        chong.add(b)
    if b in chong:
        chong.add(a)
print(len(chong))