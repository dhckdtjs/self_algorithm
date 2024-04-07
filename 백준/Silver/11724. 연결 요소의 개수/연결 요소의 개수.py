# 연결 요소의 개수
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
adj_arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    s,e = map(int,input().strip().split())
    adj_arr[s].append(e)
    adj_arr[e].append(s)

from collections import deque
def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        v = q.popleft()
        for w in adj_arr[v]:
            if visited[w] == 1:
                continue
            visited[w] = 1
            q.append(w)


cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        cnt+=1
print(cnt)