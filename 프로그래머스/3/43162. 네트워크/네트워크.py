from collections import deque
    
def bfs(i,adj_arr,visited):
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        v= q.popleft()
        for w in adj_arr[v]:
            if visited[w] == 1:
                continue
            visited[w] = 1
            q.append(w)



def solution(n, computers):
    visited = [0]*(n+1)
    adj_arr = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                adj_arr[i+1].append(j+1)
    cnt = 0
    for k in range(1,n+1):
        if visited[k] == 0:
            bfs(k,adj_arr,visited)
            cnt+=1
    return cnt


