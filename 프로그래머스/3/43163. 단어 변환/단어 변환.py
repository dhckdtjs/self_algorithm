from collections import deque
def solution(begin, target, words):
    n = len(words)
    m = len(begin)
    if target not in words:
        return 0
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        cnt = 0
        for idx in range(m):
            if begin[idx] == words[i][idx]:
                cnt+=1
        if cnt == m-1:
            graph[0].append(i+1)
            graph[i+1].append(0)
    for i in range(n-1):
        for j in range(i+1,n):
            cnt = 0
            for idx in range(m):
                if words[i][idx] == words[j][idx]:
                    cnt+=1
            if cnt== m-1:
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)
    
    def bfs(i):
        q = deque()
        q.append((i,0))
        visited = [0]*(n+1)
        visited[i] = 1
        while q:
            v,cnt = q.popleft()
            if v == 0:
                current = begin
            else:
                current = words[v-1]
            if current == target:
                return cnt
            for w in graph[v]:
                if visited[w] == 0:
                    visited[w] = 1
                    q.append((w,cnt+1))
            print(visited)
        
        return 0
        
    return bfs(0)
          