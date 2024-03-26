# 헌내기는 친구가 필요해
import sys
input = sys.stdin.readline
from collections import deque

n, m =map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]
def find_start():
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 'I':
                return row,col

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def find_path(r,c):
    q= deque()
    q.append((r,c))
    arr[r][c] = 'X'
    cnt = 0
    while q:
        row,col = q.popleft()

        for k in range(4):
            nr = row+dr[k]
            nc = col+dc[k]
            if 0<=nr<n and 0<=nc<m:
                if arr[nr][nc]=='O':
                    arr[nr][nc] ='X'
                    q.append((nr,nc))
                if arr[nr][nc] == 'P':
                    arr[nr][nc] = 'X'
                    q.append((nr,nc))
                    cnt += 1


    return cnt


r,c = find_start()
# print(r,c)
ans = find_path(r,c)
if ans ==0:
    print('TT')
else:
    print(ans)