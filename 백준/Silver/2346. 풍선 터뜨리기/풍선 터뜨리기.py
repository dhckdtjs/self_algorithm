# 풍선 터뜨리기
# 풍선 원형, 돌리면서 터뜨리고 그 인덱스 출력
from collections import deque
N = int(input())

ballon = deque(enumerate(map(int,input().split())))
# enumerate : 순서가 있는 자료형을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴
index_list = []
for _ in range(N):
    index,paper = ballon.popleft()
    index_list.append(index+1)
    if paper>0:
        ballon.rotate(-(paper-1))
    elif paper<0:
        ballon.rotate(-paper)

print(*index_list)


    
