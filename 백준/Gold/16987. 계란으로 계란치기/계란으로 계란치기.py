# 계란으로 계란치기
# 계란을 치면 무게만큼 내구도 깎임
import sys
input = sys.stdin.readline
n = int(input())
egg = []

def egg_break(idx,cnt):
    global max_cnt
    if idx == n:
        max_cnt = max(max_cnt,cnt)
        return

    if egg[idx][0]<=0:
        egg_break(idx+1,cnt)
    else:
        flag = False

        for i in range(n):
            if i != idx and egg[i][0]>0:
                egg[idx][0] -= egg[i][1]
                egg[i][0] -= egg[idx][1]
                next_cnt = cnt
                if egg[idx][0]<=0:
                    next_cnt+=1
                if egg[i][0]<=0:
                    next_cnt+=1
                flag = True
                egg_break(idx+1,next_cnt)
                egg[idx][0]+=egg[i][1]
                egg[i][0]+=egg[idx][1]
        if flag == False:
            egg_break(idx+1,cnt)

for _ in range(n):
    s,w = map(int,input().strip().split())
    egg.append([s,w])
max_cnt = 0
egg_break(0,0)
print(max_cnt)