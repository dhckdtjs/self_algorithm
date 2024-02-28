# 수 정렬하기 3
import sys
input = sys.stdin.readline
n = int(input())
arr = [0]*10001
for _ in range(n):
    arr[int(input())]+=1

for i in range(len(arr)):
    if arr[i] !=0:
        for k in range(arr[i]):
            print(i)