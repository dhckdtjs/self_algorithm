import sys
input = sys.stdin.readline
n = int(input())
num_lst = []
for i in range(n):
    num = int(input())
    num_lst.append(num)
num_lst.sort(reverse=True)
for k in num_lst:
    print(k)