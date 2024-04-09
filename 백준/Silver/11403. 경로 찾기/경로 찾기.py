# 경로 찾기
import sys
input = sys.stdin.readline
n = int(input())
adj_arr = [[] for _ in range(n+1)]

from collections import deque
def bfs(i):
    q = deque()
    q.append(i)
    while q:
        v = q.popleft()
        for w in adj_arr[v]:
            if visited[w] == 1:
                continue
            visited[w] = 1
            q.append(w)
for i in range(1,n+1):
    arr = list(map(int,input().strip().split()))
    for k in range(1,n+1):
        if arr[k-1] == 1:
            adj_arr[i].append(k)
# print(adj_arr)
for i in range(1,n+1):
    visited = [0] * (n + 1)
    bfs(i)
    print(*visited[1:])