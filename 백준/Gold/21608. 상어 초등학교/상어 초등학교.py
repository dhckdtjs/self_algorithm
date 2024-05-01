# 상어 초등학교
import sys
input = sys.stdin.readline
n = int(input())
arr = [[0]*n for _ in range(n)]

dr = [-1,0,0,1]
dc = [0,-1,1,0]
students = {}
def find_place(lst):
    seat = []
    max_cnt = -1
    max_empty = -1
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0:
                cnt = 0
                empty = 0
                for k in range(4):
                    nr = r+dr[k]
                    nc = c+dc[k]
                    if 0<=nr<n and 0<=nc<n:
                        if arr[nr][nc] == 0:
                            empty+=1
                        elif arr[nr][nc] in friends:
                            cnt+=1
                    if cnt>max_cnt or (cnt==max_cnt and empty>max_empty):
                        max_cnt = cnt
                        max_empty = empty
                        seat = [(r,c)]
                    elif cnt==max_cnt and empty==max_empty:
                        seat.append((r,c))
    seat.sort()
    return seat[0]

for i in range(n**2):
    lst = list(map(int,input().strip().split()))
    student = lst[0]
    friends = lst[1:]
    students[student] = friends
    if i == 0:
        arr[1][1] = lst[0]
    else:
        place = find_place(lst)
        arr[place[0]][place[1]] = lst[0]

total= 0
for r in range(n):
    for c in range(n):
        student = arr[r][c]
        if student in students:
            friends = students[student]
            cnt = 0
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] in friends:
                    cnt += 1
            if cnt>0:
                total += 10**(cnt-1)
print(total)