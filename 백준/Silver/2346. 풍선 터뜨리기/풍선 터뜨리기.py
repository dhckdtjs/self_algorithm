from collections import deque
N = int(input())

ballon = deque(enumerate(map(int,input().split())))
index_list = []
for _ in range(N):
    index,paper = ballon.popleft()
    index_list.append(index+1)
    if paper>0:
        ballon.rotate(-(paper-1))
    elif paper<0:
        ballon.rotate(-paper)

print(*index_list)


    
