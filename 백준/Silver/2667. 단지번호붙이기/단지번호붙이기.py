# 단지 번호 붙이기
from collections import deque
import sys

dc = [0,0,-1,1]
dr = [1,-1,0,0]


def bfs(row,col):
    q = deque()
    q.append([row,col])
    apart[row][col] = 3
    cnt = 1
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<n and 0<=nc<n and apart[nr][nc] == '1':
                apart[nr][nc] =3
                q.append([nr,nc])
                cnt+=1
    return cnt

def quick_sort(target):
    N = len(target)
    if N<=1:
        return target
    left = []
    right = []
    p_idx = N//2
    pivot = target[p_idx]
    for idx in range(N):
        if idx == p_idx: continue
        elif target[idx]<pivot:
            left.append(target[idx])
        else:
            right.append(target[idx])
    return quick_sort(left)+[pivot]+quick_sort(right)


input = sys.stdin.readline
n = int(input())
apart = [list(input()) for _ in range(n)]
group_house = []
for row in range(n):
    for col in range(n):
        if apart[row][col] == '1':
            group_house.append(bfs(row,col))
res = quick_sort(group_house)
print(len(res))
for k in res:
    print(k)