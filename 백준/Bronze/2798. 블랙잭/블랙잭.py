# 블랙잭
N,M = map(int,input().split())

card_list = list(map(int,input().split()))
card_list.sort()
s = 0
Max_res = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for l in range(j+1,N):
            s=card_list[i]+card_list[j]+card_list[l]
            if Max_res<s<=M:
                Max_res = s
                break
print(Max_res)
            