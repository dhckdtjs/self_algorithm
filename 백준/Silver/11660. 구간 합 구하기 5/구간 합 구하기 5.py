# 구간 합 구하기 5
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1]
dy = [1,0]
visited = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        visited[i][j] = visited[i-1][j]+visited[i][j-1]+arr[i-1][j-1]-visited[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(visited[x2][y2]-visited[x1-1][y2]-visited[x2][y1-1]+visited[x1-1][y1-1])
