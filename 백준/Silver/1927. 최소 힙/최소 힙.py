import heapq
import sys
input = sys.stdin.readline
pq = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(pq) == 0:
            print(0)
        else:
            k =heapq.heappop(pq)
            print(k)
    else:
        heapq.heappush(pq,num)
