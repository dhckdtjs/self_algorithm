# 킹
# 8*8 체스판

def check_loc(chr):
    for i in chr:
        if i == 'A':
            col = 0
        elif i == 'B':
            col = 1
        elif i == 'C':
            col =2
        elif i == 'D':
            col = 3
        elif i == 'E':
            col = 4
        elif i == 'F':
            col = 5
        elif i == 'G':
            col = 6
        elif i == 'H':
            col = 7
        elif i == '1':
            row = 0
        elif i == '2':
            row = 1
        elif i == '3':
            row = 2
        elif i == '4':
            row = 3
        elif i == '5':
            row = 4
        elif i == '6':
            row = 5
        elif i == '7':
            row = 6
        else:
            row = 7
    return row,col
def check_chess(row,col):
    if col == 0:
        front = 'A'
    if col == 1:
        front = 'B'
    if col == 2:
        front = 'C'
    if col == 3:
        front = 'D'
    if col == 4:
        front = 'E'
    if col == 5:
        front = 'F'
    if col == 6:
        front = 'G'
    if col == 7:
        front = 'H'
    if row == 0:
        Back = '1'
    if row == 1:
        Back = '2'
    if row == 2:
        Back = '3'
    if row == 3:
        Back = '4'
    if row == 4:
        Back = '5'
    if row == 5:
        Back = '6'
    if row == 6:
        Back = '7'
    if row == 7:
        Back = '8'
    return front+Back
def check_step(chr,row,col):
    if chr == 'R':
        row,col = row,col+1
    elif chr == 'L':
        row,col = row,col-1
    elif chr =='B':
        row,col = row-1,col
    elif chr == 'T':
        row,col = row+1,col
    elif chr == 'RT':
        row,col = row+1,col+1
    elif chr == 'LT':
        row,col = row+1,col-1
    elif chr == 'RB':
        row,col = row-1,col+1
    else:
        row,col = row-1,col-1
    return row,col
K,S,N = list(map(str,input().split()))
num = int(N)


K_row,K_col = check_loc(K)
S_row,S_col = check_loc(S)

for _ in range(num):
    step= str(input())
    prev_row,prev_col = K_row,K_col
    new_row,new_col = check_step(step,K_row,K_col)
    if 0<=new_row<8 and 0<=new_col<8:
        K_row,K_col = new_row,new_col
    else:
        continue
    if K_row == S_row and K_col == S_col:
        new2_row,new2_col = check_step(step,S_row,S_col)
        if new2_row<0 or new2_row>7 or new2_col<0 or new2_col>7:
            if S_row == K_row and K_col == S_col:
                K_row,K_col = prev_row,prev_col
        elif 0<=new2_row<8 and 0<=new2_col<8:
            S_row,S_col = new2_row,new2_col
Kres =check_chess(K_row,K_col)
Sres =check_chess(S_row,S_col)
print(Kres)
print(Sres)