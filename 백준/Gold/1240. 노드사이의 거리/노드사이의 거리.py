# 노드사이의 거리
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
adj_arr = [[] for _ in range(n+1)]
from collections import deque
def check_dis(s,e):
    visited = [-1] * (n + 1)
    q = deque()
    q.append([s,0])
    while q:
        v,dist = q.popleft()
        if v == e:
            return dist
        for j,w in adj_arr[v]:
            if visited[j]==-1:
                visited[j]=dist+w
                q.append([j,dist+w])
    return visited[e]

for i in range(n-1):
    s,e,w = map(int,input().strip().split())
    adj_arr[s].append([e,w])
    adj_arr[e].append([s,w])
for k in range(m):
    dis_s,dis_e = map(int,input().strip().split())
    ans=check_dis(dis_s,dis_e)
    print(ans)


