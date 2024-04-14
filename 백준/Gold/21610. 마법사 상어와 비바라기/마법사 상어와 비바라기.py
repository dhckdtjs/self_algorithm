# 마법사 상어와 비바라기
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]

dr = [0,0,-1,-1,-1,0,1,1,1]
dc = [0,-1,-1,0,1,1,1,0,-1]
# 구름 생성
def start(lst,di,s):
    new_lst = set()
    for r,c in lst:
        nr = (r+dr[di]*s)%n
        nc = (c+dc[di]*s)%n
        new_lst.add((nr,nc))
        arr[nr][nc]+=1
    return new_lst

dr1 = [-1,-1,1,1]
dc1 = [-1,1,1,-1]

# 물 복사
def water_copy(lst):
    for r,c in lst:
        cnt = 0
        for k in range(4):
            nr = r+dr1[k]
            nc = c+dc1[k]
            if 0<=nr<n and 0<=nc<n:
                if arr[nr][nc]>0:
                    cnt+=1
        arr[r][c]+=cnt


save_idx = {(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)}

for i in range(m):
    di,s = map(int,input().split())
    if i == 0:
        res = start(save_idx,di,s)
        save_idx = res
        # print(save_idx)
        water_copy(save_idx)

    else:
        new_idx = set()
        for r in range(n):
            for c in range(n):
                if arr[r][c]>=2:
                    if (r,c) in save_idx:
                        continue
                    new_idx.add((r,c))
                    arr[r][c]-=2

        save_idx = new_idx
        res =start(save_idx,di,s)
        save_idx = res
        # print(save_idx)
        water_copy(save_idx)


total = 0
for r in range(n):
    for c in range(n):
        if arr[r][c]>=2:
            if (r, c) in save_idx:
                continue
            arr[r][c]-=2
    total +=sum(arr[r])
print(total)
