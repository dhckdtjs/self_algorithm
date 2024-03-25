# 큐 2
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue=deque()
for _ in range(n):
    act = input().strip()
    if 'push' in act:
        num = act.split()[1]
        queue.append(num)
    elif act == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif act == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif act == 'size':
        print(len(queue))
    elif act == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif act =='pop':
        if len(queue) == 0:
            print(-1)
        else:
            i = queue.popleft()
            print(i)