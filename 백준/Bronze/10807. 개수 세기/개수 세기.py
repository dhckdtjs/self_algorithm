# 개수 세기
n = int(input())
num_list = map(int,input().split())
target = int(input())
cnt = 0
for k in num_list:
    if target == k:
        cnt+=1
print(cnt)