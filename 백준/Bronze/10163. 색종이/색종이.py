# 색종이
# 색종이를 겹겹이 쌓는다.
# 보이는 면적을 각각 구하기
# input = 가장 아래 좌표, 너비, 높이
import sys
input = sys.stdin.readline
n = int(input())
paper = [[0]*1001 for _ in range(1001)]
for i in range(1,n+1):
    x,y,width,height = map(int,input().split())
    for row in range(y,height+y):
        paper[row][x:x+width]=[i]*width
for target in range(1, n+1):
    cnt = 0
    for i in range(1001):
        cnt += paper[i].count(target)
    print(cnt)