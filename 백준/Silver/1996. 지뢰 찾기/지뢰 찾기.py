# 지뢰 찾기
import sys
input = sys.stdin.readline
n = int(input())

dr = [0,0,-1,1,-1,-1,1,1]
dc = [1,-1,0,0,-1,1,-1,1]

mine = [list(input().strip()) for _ in range(n)]
draw = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if mine[r][c] !='.':
            draw[r][c] = '*'
            temp = int(mine[r][c])
            for k in range(8):
                nr = r+dr[k]
                nc = c+dc[k]
                if 0<=nr<n and 0<=nc<n:
                    if draw[nr][nc] == '*' or draw[nr][nc] =='M':
                        continue
                    elif draw[nr][nc] ==0 and mine[nr][nc] =='.':
                        draw[nr][nc] = temp
                    elif draw[nr][nc] >=0 and mine[nr][nc] == '.':
                        draw[nr][nc]=draw[nr][nc]+temp
                        if draw[nr][nc]>=10:
                            draw[nr][nc] = 'M'
for l in draw:
    k = ''
    for j in l:
        k+=str(j)
    print(k)