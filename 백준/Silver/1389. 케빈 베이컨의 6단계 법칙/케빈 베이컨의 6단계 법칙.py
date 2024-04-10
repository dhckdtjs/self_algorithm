# 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
adj_arr = [[] for _ in range(n+1)]
from collections import deque

def find_friends(i,e,cnt):
    q= deque()
    visited = [0]*(n+1)
    q.append((i,cnt))
    visited[i] = 1
    while q:
        v,cnt = q.popleft()
        for w in adj_arr[v]:
            if w == e:
                return cnt+1
            if visited[w] == 1:
                continue
            visited[w] = 1
            q.append((w,cnt+1))
    return cnt


for i in range(m):
    s,e = map(int,input().strip().split())
    adj_arr[s].append(e)
    adj_arr[e].append(s)
# print(adj_arr)
ans = [0]*(n+1)
for k in range(1,n+1):
    for j in range(1,n+1):
        if k==j:
            continue
        # print(k,j)
        res = find_friends(k,j,0)
        ans[k]+=res
min_value = float('inf')
for k in range(n,0,-1):
    if min_value>=ans[k]:
        min_value = ans[k]
        idx = k
print(idx)