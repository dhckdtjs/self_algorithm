# 듣보잡
import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
dont_h = set()
for i in range(n):
    person = input().rstrip()
    dont_h.add(person)
dont_s = set()
for _ in range(m):
    person = input().rstrip()
    dont_s.add(person)
ans = sorted(dont_h & dont_s)
print(len(ans))
for k in ans:
    print(k)