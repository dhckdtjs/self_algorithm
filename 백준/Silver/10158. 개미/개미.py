w, h =map(int,input().split()) # 격자 크기
p,q = map(int,input().split()) # 초기 위치
t = int(input())               # 시간
width = []
height = []
for i in range(w+1):
    width.append(i)
for i in range(w-1,0,-1):
    width.append(i)
for j in range(h+1):
    height.append(j)
for j in range(h-1,0,-1):
    height.append(j)
result_x = (p+t)%len(width)
result_y = (q+t)%len(height)
print(width[result_x],height[result_y])