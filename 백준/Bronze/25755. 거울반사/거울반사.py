# 거울반사
w,n = input().split()
n = int(n)
arr = [list(map(int,input().split())) for _ in range(n)]
paper = [[0]*n for _ in range(n)]
one_lst = []
two_lst = []
five_lst = []
eight_lst = []
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            one_lst.append([r,c])
        if arr[r][c] == 2:
            two_lst.append([r,c])
        if arr[r][c] == 5:
            five_lst.append([r,c])
        if arr[r][c] == 8:
            eight_lst.append([r,c])

if w == 'D'or w=='U':
    for r1,c1 in one_lst:
        r1 = n-r1-1
        paper[r1][c1] = 1
    for r2,c2 in two_lst:
        r2 = n-r2-1
        paper[r2][c2] = 5

    for r5,c5 in five_lst:
        r5 = n-r5-1
        paper[r5][c5] = 2
    for r8,c8 in eight_lst:
        r8 = n-r8-1
        paper[r8][c8] = 8
elif w =='R' or w=='L':
    for r1, c1 in one_lst:
        c1 = n - c1 - 1
        paper[r1][c1] = 1
    for r2, c2 in two_lst:
        c2 = n - c2 - 1
        paper[r2][c2] = 5

    for r5, c5 in five_lst:
        c5 = n - c5 - 1
        paper[r5][c5] = 2
    for r8, c8 in eight_lst:
        c8 = n - c8 - 1
        paper[r8][c8] = 8
for r in range(n):
    for c in range(n):
        if paper[r][c] == 0:
            paper[r][c] ='?'
for l in paper:
    print(*l)