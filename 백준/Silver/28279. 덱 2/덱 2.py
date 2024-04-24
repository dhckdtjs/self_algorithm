# 덱 2
import sys
input = sys.stdin.readline
n = int(input())
from collections import deque
def function(a,b):
    if a == 1:
        q.appendleft(b)
    elif a == 2:
        q.append(b)
    elif a == 3:
        if q:
            i = q.popleft()
            print(i)
        else:
            print(-1)
    elif a==4:
        if q:
            i = q.pop()
            print(i)
        else:
            print(-1)
    elif a == 5:
        print(len(q))
    elif a == 6:
        if q:
            print(0)
        else:
            print(1)
    elif a == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif a== 8:
        if q:
            print(q[-1])
        else:
            print(-1)


q = deque()

for _ in range(n):
    a = input().split()
    if len(a) == 1:
        function(int(a[0]),0)
    else:
        function(int(a[0]),int(a[1]))