# 맥주 마시면서 걸어가기
T = int(input())
from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        if abs(cx-rock_x)+abs(cy-rock_y) <= 1000:
            return 'happy'
        for i in range(n):
            if i not in visited:
                new_x,new_y = cu[i]
                if abs(cx-new_x)+abs(cy-new_y)<=1000:
                    q.append(cu[i])
                    visited.add(i)
    return 'sad'

for tc in range(1,T+1):
    n = int(input())
    house_x,house_y = map(int,input().split())
    cu = [list(map(int,input().split())) for _ in range(n)]
    rock_x,rock_y = map(int,input().split())
    visited = set()
    res = bfs(house_x,house_y)
    print(res)