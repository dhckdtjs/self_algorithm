# 블랙잭
N,M = map(int,input().split())
card_list = list(map(int,input().split()))
card_list.sort()

Max_sum = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            res = card_list[i]+card_list[j]+card_list[k]
            if Max_sum<res<=M:
                Max_sum = res
print(Max_sum)