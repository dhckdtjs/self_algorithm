# 검증수
num_list = list(map(int,input().split()))
Sum_sq = 0
for k in num_list:
    Sum_sq+=k**2

print(Sum_sq%10)