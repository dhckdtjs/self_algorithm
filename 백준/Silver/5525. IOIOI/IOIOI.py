# IOIOI
import sys
input = sys.stdin.readline
n = int(input())
check = 'IO'*n+'I'
m = int(input())
sen = input().strip()
# print(sen)
l = len(check)
cnt = 0
for k in range(m):
    stack = []
    if sen[k] == 'I':
        stack.append(sen[k:k+l])
        if stack == [check]:
            cnt+=1
print(cnt)