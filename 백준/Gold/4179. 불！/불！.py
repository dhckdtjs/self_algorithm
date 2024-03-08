from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]
human = [[0] * C for _ in range(R)]
fire = [[0] * C for _ in range(R)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

q_f = deque()
q_j = deque()

for row in range(R):
    for col in range(C):
        if maze[row][col] == 'F':
            q_f.append((row, col))
            fire[row][col] = 1
        elif maze[row][col] == 'J':
            q_j.append((row, col))
            human[row][col] = 1

def bfs_fire():
    while q_f:
        r, c = q_f.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#' and fire[nr][nc] == 0:
                fire[nr][nc] = fire[r][c] + 1
                q_f.append((nr, nc))

def bfs_human():
    while q_j:
        r, c = q_j.popleft()
        if r == 0 or r == R-1 or c == 0 or c == C-1:  # 탈출 조건
            print(human[r][c])
            return
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#' and human[nr][nc] == 0:
                if fire[nr][nc] == 0 or human[r][c] + 1 < fire[nr][nc]:
                    human[nr][nc] = human[r][c] + 1
                    q_j.append((nr, nc))
    print("IMPOSSIBLE")

bfs_fire()
bfs_human()
