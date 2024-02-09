# 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
people = deque()
for i in range(1,n+1):
    people.append(i)
print('<',end='')
for j in range(1,n+1):
    people.rotate(-(k-1))
    kill = people.popleft()
    print(kill,end='')
    while j <n:
        print(',',end=' ')
        break
print('>')