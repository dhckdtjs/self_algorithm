# 가장 가까운 세 사람의 심리적 거리
from itertools import combinations
T = int(input())
import sys
input = sys.stdin.readline

def check_dis(path):
    ans = 0
    for k in range(4):
        if path[0][k] != path[1][k]:
            ans+=1
        if path[0][k] != path[2][k]:
            ans+=1
        if path[1][k] != path[2][k]:
            ans+=1
    return ans

for tc in range(1,T+1):
    n = int(input())
    mbti = list(input().strip().split())
    path = []
    min_v = float('inf')
    if n>32:
        min_v = 0
    else:
        for comb in combinations(mbti,3):
            res = check_dis(comb)
            min_v = min(res,min_v)
            if min_v<=res:
                continue
            min_v = res
    print(min_v)