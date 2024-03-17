# 가로수
import sys
input = sys.stdin.readline
n = int(input())
lst = [0]*n
for i in range(n):
    tree = int(input())
    lst[i] = tree
temp_lst = [0]*(n-1)
for j in range(n-1):
    temp = lst[j+1]-lst[j]
    temp_lst[j] = temp
l = 1
Max = 0
def find_Max(num1,num2):
    while num2!=0:
        num1,num2 = num2,num1%num2
    return num1
temp_lst.sort(reverse=True)
Min_res = float('inf')
for i in range(n-2):
    for j in range(i+1,n-1):
        res = find_Max(temp_lst[i],temp_lst[j])
        if Min_res>res:
            Min_res = res
        elif Min_res<=res:
            break
cnt = 0
for k in temp_lst:
    cnt+=(k//Min_res)-1
print(cnt)