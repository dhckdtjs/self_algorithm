# 양
import sys
input = sys.stdin.readline
r,c = map(int,input().strip().split())
arr = [list(input().strip()) for _ in range(r)]

dr = [0,0,-1,1]
dc = [1,-1,0,0]
from collections import deque

def bfs(cur_r,cur_c,flag):
    q = deque()
    if flag == 1:
        cntw = 1
        cnts = 0
    elif flag == 2:
        cntw = 0
        cnts = 1
    q.append((cur_r,cur_c))
    arr[cur_r][cur_c] = 'c'
    while q:
        cr,cc = q.popleft()
        for k in range(4):
            nr = cr+dr[k]
            nc = cc+dc[k]
            if 0<=nr<r and 0<=nc<c:
                if arr[nr][nc] == '.':
                    arr[nr][nc] = 'c'
                    q.append((nr,nc))
                elif arr[nr][nc] =='v':
                    arr[nr][nc] = 'c'
                    cntw+=1
                    q.append((nr,nc))
                elif arr[nr][nc] == 'o':
                    arr[nr][nc] = 'c'
                    cnts+=1
                    q.append((nr,nc))
    return cntw,cnts



total_w = 0
total_s = 0
for row in range(r):
    for col in range(c):
        if arr[row][col] == 'v':
            tempw,temps = bfs(row,col,1)
            if tempw>=temps:
                temps = 0
            else:
                tempw = 0
            total_w+=tempw
            total_s+=temps
        elif arr[row][col] == 'o':
            tempw,temps = bfs(row,col,2)
            if tempw>=temps:
                temps = 0
            else:
                tempw = 0
            total_w+=tempw
            total_s+=temps
print(total_s,total_w)