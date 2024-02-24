from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def bfs(row, col):
    q = deque()
    q.append([row, col])
    cnt = 1  # 시작 지점을 이미 포함하므로 1부터 시작
    paper[row][col] = 3  # 방문 표시

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and paper[nr][nc] == 1:
                q.append([nr, nc])
                paper[nr][nc] = 3
                cnt += 1
    return cnt

pictures = []
for row in range(n):
    for col in range(m):
        if paper[row][col] == 1:  # 탐색되지 않은 그림 발견
            pictures.append(bfs(row, col))

if pictures:
    print(len(pictures))
    print(max(pictures))
else:
    print(0)
    print(0)
