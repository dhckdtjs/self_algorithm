# 로봇 청소기
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
r,c,dir = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def find_path(r,c,dir):
    cnt = 1
    arr[r][c] = 2
    while True:
        flag = 0
        for k in range(4):
            dir = (dir+3)%4
            nr = r+dr[dir]
            nc = c+dc[dir]
            if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                cnt+=1
                r = nr
                c = nc
                flag = 1
                break
        if flag == 0:
            if arr[r-dr[dir]][c-dc[dir]] == 1:
                print(cnt)
                break
            else:
                r,c = r-dr[dir],c-dc[dir]

find_path(r,c,dir)
