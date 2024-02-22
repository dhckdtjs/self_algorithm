# 킹,퀸,룩,비숍,나이트,폰
chess = [1,1,2,2,2,8]
num = list(map(int,input().split()))
for k in range(len(num)):
    print(chess[k]-num[k],end=' ')