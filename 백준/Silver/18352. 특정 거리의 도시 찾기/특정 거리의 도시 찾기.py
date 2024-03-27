import sys
input = sys.stdin.readline
from heapq import heappush,heappop
# n 도시 개수 m 도로 개수 k 거리 정보 x 출발 도시 번호
n,m,k,x = map(int,input().strip().split())
adj_arr = [[] for _ in range(n+1)]
visited = [-float('inf')]*(n+1)

def dijsktra(i):
    pq = []
    heappush(pq,(0,i))
    visited[i] = 0
    while pq:
        cnt,v = heappop(pq)
        if cnt<visited[v]:
            continue
        for j in adj_arr[v]:
            if visited[j]==-float('inf'):
                visited[j] = cnt+1
                heappush(pq,(cnt+1,j))



for i in range(m):
    st,ed = map(int,input().strip().split())
    adj_arr[st].append(ed)
dijsktra(x)
res = []
for q in range(1,n+1):
    if visited[q] == k:
        res.append(q)
        print(q)
if not res:
    print(-1)
