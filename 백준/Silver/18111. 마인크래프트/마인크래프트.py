import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
land = [list(map(int,input().split())) for _ in range(N)]
answer = sys.maxsize
idx = 0
for target in range(257):
    max_target,min_target = 0,0
    for row in range(N):
        for col in range(M):
            if land[row][col]>=target:
                max_target +=land[row][col]-target
            else:
                min_target +=target-land[row][col]
    if max_target+B >=min_target:
        if min_target+(max_target*2)<=answer:
            answer = min_target+(max_target*2)
            idx = target
print(answer,idx)
