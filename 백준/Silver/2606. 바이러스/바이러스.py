# 바이러스
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,V):
    visited=[0]*(V+1)
    q = deque()
    q.append(i)
    visited[i] = 1
    cnt = 0
    while q:
        t=q.popleft()
        if t !=i:
            cnt+=1
        for j in adj_arr[t]:
            if visited[j] ==0:
                q.append(j)
                visited[j] = 1
    return cnt

V = int(input())
E = int(input())
adj_arr = [[] for _ in range(V+1)]
for i in range(E):
    start,end = map(int,input().split())
    adj_arr[start].append(end)
    adj_arr[end].append(start)
print(bfs(1,V))
