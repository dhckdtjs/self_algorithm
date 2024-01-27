import sys
input = sys.stdin.readline
num_list = []
n = int(input())
for k in range(n):
    N = int(input())
    num_list.append(N)
num_list.sort()
for k in num_list:
    print(k)