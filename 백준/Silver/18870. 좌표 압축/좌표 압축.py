# 좌표 압축
import sys
input =sys.stdin.readline
n = int(input())
num = list(map(int,input().strip().split()))
num_dict = {}
cnt = 0
k = 0
temp = sorted(num)
for i in temp:
    if i not in num_dict:
        num_dict[i] = k
    else:
        continue
    k+=1
# print(num_dict)
for j in num:
    print(num_dict[j],end=' ')