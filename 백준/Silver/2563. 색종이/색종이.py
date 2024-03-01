# 색종이
paper = [[0]*100 for _ in range(100)]
n = int(input())
for _ in range(n):
    r,c = map(int,input().split())
    for row in range(r,r+10):
        for col in range(c,c+10):
            paper[row][col] =1
    res = 0
    for row in range(100):
        res +=paper[row].count(1)
print(res)