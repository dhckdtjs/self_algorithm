# 기상캐스터
row, col = map(int,input().split())
dr = 0
dc = 1
sky = [list(map(str,input())) for _ in range(row)]
check_c = [[0]*col for _ in range(row)]
for r in sky:
    if r.count('c') == 0:
        for c in range(col):
            r[c] = -1
    for c in range(col):
        if r[c] == 'c':
            r[c] = 0
for i in range(row):
    for j in range(col):
        if sky[i][j] == '.':
            if j == 0:
                sky[i][j] = -1
            else:
                if sky[i][j-1]==-1:
                    sky[i][j]=-1
                elif sky[i][j-1] == 0:
                    sky[i][j] = 1
                else:
                    sky[i][j]=sky[i][j-1]+1
for k in sky:
    print(*k)