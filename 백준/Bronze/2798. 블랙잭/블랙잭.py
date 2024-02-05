N,M = map(int,input().split())
card_list = list(map(int,input().split()))
Max_result = 0
for i in range(len(card_list)):
    for j in range(i+1,len(card_list)):
        for k in range(j+1,len(card_list)):
            if card_list[i]+card_list[j]+card_list[k] == M:
                Max_result = M
            elif card_list[i]+card_list[j]+card_list[k] <M:
                result = card_list[i]+card_list[j]+card_list[k]
                if Max_result<result:
                    Max_result = result

print(Max_result)