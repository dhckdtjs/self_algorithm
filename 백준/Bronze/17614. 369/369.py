# 369
# 3.6,9가 나오면 박수 횟수 +1
# 총 박수 횟수 계산
import sys
input = sys.stdin.readline
n = int(input())
result = 1
cnt = 0
while result<=n:
    check = str(result)
    for k in check:
        if k == '3':
            cnt+=1
        if k == '6':
            cnt+=1
        if k == '9':
            cnt+=1
    if result == n:
        break
    result+=1
print(cnt)