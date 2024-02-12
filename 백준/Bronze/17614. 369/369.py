# 369
# 3.6,9가 나오면 박수 횟수 +1
# 총 박수 횟수 계산
n = int(input())
result = 1
cnt = 0
while result<=n:
    for k in str(result):
        if k == '3':
            cnt+=1
        if k == '6':
            cnt+=1
        if k == '9':
            cnt+=1
    result+=1
print(cnt)