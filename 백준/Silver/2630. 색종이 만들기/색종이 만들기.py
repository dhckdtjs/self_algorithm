# 색종이 만들기
import sys
input = sys.stdin.readline
n = int(input())

arr = [list(map(int,input().strip().split())) for _ in range(n)]

def dfs(r,c,i):
    global cnt1
    global cnt0
    fir = arr[r][c]
    for row in range(r,r+i):
        for col in range(c,c+i):
            if fir != arr[row][col]:
                dfs(r,c,i//2)
                dfs(r+i//2,c,i//2)
                dfs(r,c+i//2,i//2)
                dfs(r+i//2,c+i//2,i//2)
                return
    if fir == 1:
        cnt1+=1
    if fir == 0:
        cnt0+=1

cnt0=0
cnt1=0
dfs(0,0,n)
print(cnt0)
print(cnt1)