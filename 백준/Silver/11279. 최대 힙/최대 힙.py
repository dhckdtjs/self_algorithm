# 최대 힙
n = int(input())
import heapq
import sys
input = sys.stdin.readline
pq = []
for _ in range(n):
    k = int(input())
    if k == 0:
        if len(pq) == 0:
            print(0)
        else:
            i = heapq.heappop(pq)
            print(-i)
    if k >0:
        heapq.heappush(pq,-k)