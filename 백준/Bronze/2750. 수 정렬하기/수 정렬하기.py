# 수 정렬하기
n = int(input())
num = [0]*n
for i in range(n):
    k = int(input())
    num[i] = k
num.sort()
for j in num:
    print(j)