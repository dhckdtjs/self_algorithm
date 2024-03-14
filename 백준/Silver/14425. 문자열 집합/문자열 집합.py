# 문자열 집합
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
word_set = set()
cnt = 0
for i in range(n):
    word_set.add(input().strip())
for j in range(m):
    k = input().strip()
    if k in word_set:
        cnt+=1
print(cnt)