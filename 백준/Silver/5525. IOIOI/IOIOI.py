# IOIOI
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
sen = input().strip()
cnt = 0
i = 0
ans = 0
while i<m-1:
    if sen[i:i+3] =='IOI':
        i+=2
        cnt+=1
        if cnt == n:
            ans+=1
            cnt-=1
    else:
        i+=1
        cnt = 0
print(ans)