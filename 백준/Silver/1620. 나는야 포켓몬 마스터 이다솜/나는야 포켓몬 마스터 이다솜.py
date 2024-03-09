# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline
pocketmon_name = {}
pocketmon_idx = {}
N,M = map(int,input().rstrip().split())
for i in range(N):
    monster = input().rstrip()
    pocketmon_name[monster] = i+1
    pocketmon_idx[i+1] =monster
for k in range(M):
    quest = input().rstrip()
    if quest.isdecimal():
        quest = int(quest)
        print(pocketmon_idx[quest])
    else:
        print(pocketmon_name[quest])
