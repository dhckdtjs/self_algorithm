# 직사각형 네개의 합집합의 면적 구하기
def square_search(arr,x1,y1,x2,y2):
    for r in range(y1,y2):          # 배열은 반대
        for c in range(x1,x2):
            arr[r][c]+=1
    return arr

square_list = []
paper= [[0]*100 for _ in range(100)]
for i in range(4):
    x1,y1,x2,y2 = list(map(int,input().split()))
    square_list.append([x1,y1,x2,y2])
    square_search(paper,square_list[i][0],square_list[i][1],square_list[i][2],square_list[i][3])
cnt = 0
for j in range(100):
    for k in range(100):
        if paper[j][k] !=0:
            cnt+=1
print(cnt)