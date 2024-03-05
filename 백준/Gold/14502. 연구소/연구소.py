# 연구소
from collections import deque
N,M = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]
k =3
path = []
def find_start():
    res = []
    for row in range(N):
        for col in range(M):
            if lab[row][col] == 2:
                res.append([row,col])
    return res

dr = [0,0,-1,1]
dc = [1,-1,0,0]


def bfs(r,c,lst):
    q = deque()
    q.append([r,c])
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<N and 0<=nc<M:
                if lst[nr][nc] == 1:
                    continue
                if lst[nr][nc] == 0:
                    lst[nr][nc] = 2
                    q.append([nr,nc])
    return lst


def permu(start,x):
    global Max_cnt
    if x == k:
        for j in path:
            lab[j[0]][j[1]] = 1
        copy_lab = [[0] * M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                copy_lab[r][c] = lab[r][c]
        virus= find_start()
        for v in virus:
            res = bfs(v[0],v[1],copy_lab)
        cnt = 0
        for z in res:
            cnt += z.count(0)
        Max_cnt = max(cnt, Max_cnt)

        for j in path:
            lab[j[0]][j[1]] = 0
        return
    for i in range(start,L):
        path.append(candidate[i])
        permu(i+1,x+1)
        path.pop()

candidate = []
for row in range(N):
    for col in range(M):
        if lab[row][col] == 0:
            candidate.append([row,col])
L = len(candidate)
Max_cnt = 0
permu(0,0)
print(Max_cnt)