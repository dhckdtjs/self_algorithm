# 빙고
import sys
input=sys.stdin.readline
def is_bingo1(arr):
    bingo_cnt1 = 0
    for i in range(5):
        Sum = 0
        for j in range(5):
            Sum+=arr[i][j]
        if Sum == 0:
            bingo_cnt1+=1
    return bingo_cnt1
def is_bingo2(arr):
    bingo_cnt2 = 0
    for j in range(5):
        Sum = 0
        for i in range(5):
            Sum+=arr[i][j]
        if Sum == 0:
            bingo_cnt2+=1
    return bingo_cnt2
def is_bingo3(arr):
    bingo_cnt3 = 0
    Sum = 0
    for i in range(5):
        Sum+=arr[i][i]
    if Sum == 0:
        bingo_cnt3+=1
    return bingo_cnt3
def is_bingo4(arr):
    bingo_cnt4 = 0
    Sum = 0    
    for i in range(5):
        Sum+=arr[i][4-i]
    if Sum == 0:
        bingo_cnt4+=1
    return bingo_cnt4
bingo = [list(map(int,input().split())) for _ in range(5)]
check = []
for _ in range(5):
    check += list(map(int,input().split())) 
cnt = 0

for h in range(25):
    now = check[h]
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == now:
                bingo[i][j] = 0
                cnt+=1
    if is_bingo1(bingo)+is_bingo2(bingo)+is_bingo3(bingo)+is_bingo4(bingo)  >= 3:
        print(cnt)
        sys.exit()
        