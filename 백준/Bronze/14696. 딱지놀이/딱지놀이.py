# 딱지놀이
# 별>동그라미>네모>세모 (4,3,2,1)
# 비기면 D
n = int(input())
for _ in range(n):
    score_A = [0]*5
    score_B = [0]*5
    A,*play_A = list(map(int,input().split()))
    B,*play_B = list(map(int,input().split()))
    play_A = list(play_A)
    play_B = list(play_B)
    for cnt_A in play_A:
        score_A[cnt_A]+=1
    for cnt_B in play_B:
        score_B[cnt_B]+=1
    for k in range(len(score_A)-1,0,-1):
        if score_A[k]>score_B[k]:
            print('A')
            break
        elif score_B[k]>score_A[k]:
            print('B')
            break
        elif score_A == score_B:
            print('D')
            break
        else:
            continue