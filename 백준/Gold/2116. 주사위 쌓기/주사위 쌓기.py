# 주사위 쌓기
# A-F, B-D, C-E 쌍
# 위 아래 숫자만 맞추면 옆면은 돌릴 수 있음
import sys
input = sys.stdin.readline
n = int(input())
dice = [list(map(int,input().split())) for _ in range(n)]
rotate = {0:5,1:3,2:4,3:1,4:2,5:0}
maximum =0
for i in range(6):
    Max1 = 0
    res = []
    temp = [1,2,3,4,5,6]
    temp.remove(dice[0][i])
    next = dice[0][rotate[i]]
    temp.remove(next)
    for num1 in temp:
        if Max1<num1:
            Max1= num1
    res.append(Max1)
    for j in range(1,n):
        Max2 = 0
        temp = [1,2,3,4,5,6]
        temp.remove(next)
        next = dice[j][rotate[dice[j].index(next)]]
        temp.remove(next)
        for num2 in temp:
            if Max2<num2:
                Max2 = num2
        res.append(Max2)
        Sum =0
    for k in res:
        Sum+=k
    if maximum<Sum:
        maximum = Sum
print(maximum)