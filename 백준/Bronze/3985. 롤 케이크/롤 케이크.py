# 롤 케이크
L = int(input())        # 롤 케이크 길이
cake = [0]*(L+1)
N = int(input())        # 방청객 수
Max_res = 0
Min_idx = N+1
for i in range(1,N+1):
    start,end = map(int,input().split())
    res = end-start+1
    if Max_res<res:
        Max_res = res
        Min_idx = i
    elif Max_res == res:
        if Min_idx>i:
            Min_idx = i
    for j in range(start,end+1):
        if cake[j] == 0:
            cake[j] = i
print(Min_idx)
temp_max = 0
real_idx = N+1
for k in range(1,N+1):
    real_max = cake.count(k)
    if temp_max<real_max:
        temp_max = real_max
        real_idx = k
    elif temp_max == real_max:
        if real_idx>k:
            real_idx = k
print(real_idx)
    