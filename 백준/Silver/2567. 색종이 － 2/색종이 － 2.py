# 색종이 2
n = int(input())
row_list = []
col_list = []
arr = [[0]*102 for _ in range(102)]
for _ in range(n):
    c,r = map(int,input().split())
    for row in range(r,r+10):
        for col in range(c,c+10):
            arr[row][col] = 1
cnt = 0
for i in arr:
    for j in range(1,len(i)):
        if i[j-1] != i[j]:
            cnt+=1
arr = list(zip(*arr))
for i in arr:
    for j in range(1,len(i)):
        if i[j-1] != i[j]:
            cnt+=1
print(cnt)