# 색종이
# 색종이를 겹겹이 쌓는다.
# 보이는 면적을 각각 구하기
# input = 가장 아래 좌표, 너비, 높이
n = int(input())
paper = [[0]*1000 for _ in range(1001)]
cnt_list = []
for i in range(1,n+1):
    x,y,width,height = map(int,input().split())
    for row in range(x,width+x):
        for col in range(y,height+y):
            paper[row][col]=i
for i in range(1,n+1):
    k=0
    for row in range(1000):
        for col in range(1000):
            if paper[row][col]== i:
                k+=1
    cnt_list.append(k)
for color in cnt_list:
    print(color)