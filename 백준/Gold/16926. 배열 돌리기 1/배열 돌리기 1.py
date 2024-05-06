import sys
from collections import deque
input = sys.stdin.readline
n,m,r = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for  _ in range(n)]
paper = [[0]*m for _ in range(n)]
l = min(m,n)//2
for i in range(l):
    q = deque()
    q.extend(arr[i][i:m-i])
    for k in range(i+1,n-i-1):
        q.append(arr[k][m-i-1])
    q.extend(arr[n-i-1][i:m-i][::-1])
    for k in range(n-i-2,i,-1):
        q.append(arr[k][i])

    q.rotate(-r)
    for j in range(i,m-i):
        paper[i][j] = q.popleft()
    for j in range(i+1,n-i-1):
        paper[j][m-i-1] = q.popleft()
    for j in range(m-i-1,i-1,-1):
        paper[n-i-1][j] = q.popleft()
    for j in range(n-i-2,i,-1):
        paper[j][i] = q.popleft()
for w in paper:
    print(' '.join(map(str,w)))
