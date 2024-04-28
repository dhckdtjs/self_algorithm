# 진우의 민트초코우유
import sys
input = sys.stdin.readline
n,m,h = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
milk = []
start_r = 0
start_c = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            start_r = r
            start_c = c
        if arr[r][c] == 2:
            milk.append((r,c))
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def find_path(r,c,s,cnt):
    global max_v
    for nr, nc in milk:
        # print(nr,nc)
        if arr[nr][nc] ==2:
            dist = abs(nr-r)+abs(nc-c)
            if dist<=s:
                arr[nr][nc] = 0
                find_path(nr,nc,s+h-dist,cnt+1)
                arr[nr][nc] = 2
    if abs(r-start_r)+abs(c-start_c)<=s:
        max_v = max(max_v,cnt)


visited = [[0]*n for _ in range(n)]
max_v = -float('inf')
find_path(start_r,start_c,m,0)
print(max_v)
