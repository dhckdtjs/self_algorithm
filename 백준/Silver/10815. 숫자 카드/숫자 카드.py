# 숫자 카드
import sys
input = sys.stdin.readline
n = int(input())
sang = list(map(int,input().strip().split()))
m = int(input())
num = list(map(int,input().strip().split()))
sang_dict ={}
for i in sang:
    sang_dict[i] = 1
for j in num:
    if j in sang_dict:
        print(1,end=' ')
    else:
        print(0,end=' ')