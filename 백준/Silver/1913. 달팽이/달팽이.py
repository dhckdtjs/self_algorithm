# 달팽이
# 2차원 리스트 받아서 달팽이 모양으로 배열 출력
# 입력 받은 자연수의 좌표를 나타내는 두 정수 출력
n = int(input())
check = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
arr = [[0]*n for _ in range(n)]
num=1
length = 1
direct= 0
r = (n//2)
c = (n//2)
arr[r][c] = num
while num < n*n:
    for _ in range(2):  # 각 거리에 대해 2번의 방향 전환 (위/오른쪽, 아래/왼쪽)
        for _ in range(length):
            if num >= n*n:
                break
            nr = r+dr[direct]
            nc = c+dc[direct]
            if 0<=nr<n and 0<=nc<n:
                num += 1
                r = nr
                c = nc
                arr[r][c] = num
        direct = (direct + 1) % 4  # 방향 전환
    length += 1  # 이동 거리 증가
for k in range(n):
    print(*arr[k])
for r in range(n):
    for c in range(n):
        if arr[r][c] == check:
            print(r+1,c+1)
            break
