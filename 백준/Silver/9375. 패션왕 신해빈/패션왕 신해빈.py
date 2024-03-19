# 패션왕 신해빈
import sys
input = sys.stdin.readline
T = int(input())

for tc in range(1,T+1):
    fashion_dict = {}
    n = int(input())
    for _ in range(n):
        name, kind = input().strip().split()
        if kind in fashion_dict:
            fashion_dict[kind]+=1
        else:
            fashion_dict[kind]= 1
    result = 1
    for i in fashion_dict:
        result *=fashion_dict[i]+1

    print(result-1)