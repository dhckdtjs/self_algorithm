# 최댓값
num_list = []
for _ in range(1,10):
    k = int(input())
    num_list.append(k)
Big = 0
for i in num_list:
    if i>Big:
        Big = i
print(Big)
print(num_list.index(Big)+1)