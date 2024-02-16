# 자리배정
x,y = map(int,input().split())
K = int(input())
seat = [[0]*x for _ in range(y)]
num = 1
dr = [-1,0,1,0]
dc = [0,1,0,-1]
direct = 0
row = y-1
col = 0
seat[row][col] = num
while num<x*y:
    nr = row+dr[direct]
    nc = col+dc[direct]
    if 0<=nr<y and 0<=nc<x and seat[nr][nc] == 0:
        num+=1
        row = nr
        col = nc
        seat[row][col] = num
    else:
        direct = (direct+1)%4

for row in range(y):
    for col in range(x):
        if K>y*x:
            print(0)
            exit(0)
        elif seat[row][col] == K:
            print(col+1,y-row)
        