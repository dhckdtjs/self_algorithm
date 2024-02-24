# 최댓값
arr = [list(map(int,input().split())) for _ in range(9)]
Max_num = -1
for row in range(9):
    for col in range(9):
        num = arr[row][col]
        if Max_num<num:
            Max_num = num
            Max_row = row
            Max_col = col
print(Max_num)
print(Max_row+1,Max_col+1)