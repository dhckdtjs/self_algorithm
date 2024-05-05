# N번째 큰수
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
n = int(input())
pq = []
for _ in range(n):
    lst = list(map(int,input().strip().split()))
    for k in lst:
        if len(pq)<n:
            heappush(pq,k)
        else:
            if pq[0]<k:
                heappop(pq)
                heappush(pq,k)
print(pq[0])