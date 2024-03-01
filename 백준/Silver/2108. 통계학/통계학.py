# 통계학
import sys
input = sys.stdin.readline
import collections
n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)
num_list.sort()
length = len(num_list)
res1 = int(round(sum(num_list)/n,0))            # 평균
res2 = num_list[(length//2)]                    # 중앙값
dictionary = collections.Counter(num_list)
max_res = max(dictionary.values())
res3_list = []
for i in dictionary:
    if dictionary[i] == max_res:
        res3_list.append(i)
if len(res3_list)>=2:
    res3 = res3_list[1]
else:
    res3 = res3_list[0]
res4 = max(num_list)- min(num_list)             # 범위

print(res1)
print(res2)
print(res3)
print(res4)