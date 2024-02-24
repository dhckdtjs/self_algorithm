# 행렬 덧셈
n,m = map(int,input().split())
arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]
new_arr = [[0]*m for _ in range(n)]
for row in range(n):
    for col in range(m):
        new_arr[row][col]=arr1[row][col]+arr2[row][col]
for k in new_arr:
    print(*k)