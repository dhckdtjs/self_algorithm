import sys
input = sys.stdin.readline
n,m,r = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
l = min(n,m)//2
from collections import deque
ans = [[0]*m for _ in range(n)]
for k in range(l):
    q = deque()
    q.extend(arr[k][k:m-k])
    for lst in arr[k+1:n-k-1]:
        q.append(lst[m-k-1])
    q.extend(arr[n-k-1][k:m-k][::-1])
    for lst in arr[k+1:n-k-1][::-1]:
        q.append(lst[k])
    q.rotate(-r)
    for j in range(k,m-k):
        ans[k][j] = q.popleft()
    for j in range(k+1,n-k-1):
        ans[j][m-k-1] = q.popleft()
    for j in range(m-k-1,k-1,-1):
        ans[n-k-1][j] = q.popleft()
    for j in range(n-k-2,k,-1):
        ans[j][k] = q.popleft()
for i in range(n):
    print(' '.join(map(str,ans[i])))