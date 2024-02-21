# DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline

def dfs(i,V):
    visited1 = [0]*(V+1)
    stack = []
    stack.append(i)
    print(i,end=' ')
    visited1[i] = 1
    while True:
        for j in adj_arr[i]:
            if visited1[j] == 0:
                stack.append(i)
                print(j,end=' ')
                visited1[j] = 1
                i = j
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break

def bfs(i,V):
    visited2 = [0]*(V+1)
    q = deque()
    q.append(i)
    visited2[i] = 1
    while q:
        t = q.popleft()
        print(t,end=' ')
        for j in adj_arr[t]:
            if visited2[j] == 0:
                visited2[j] = 1
                q.append(j)


V,E,N = map(int,input().split())
adj_arr= [[] for _ in range(V+1)]
for i in range(E):
    start,end = map(int,input().split())
    adj_arr[start].append(end)
    adj_arr[end].append(start)
for k in adj_arr:
    k.sort()
dfs(N,V)
print()
bfs(N,V)
print()