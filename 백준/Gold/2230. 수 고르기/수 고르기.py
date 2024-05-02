import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)
num_list.sort()
a = 0
b = 1
min_v = float('inf')
if len(num_list) == 2:
    min_v = num_list[b]-num_list[a]
else:
    while b<n:
        if num_list[b]-num_list[a]==m:
            min_v= m
            break
        elif num_list[b]-num_list[a]>m:
            min_v = min(min_v,num_list[b]-num_list[a])
            a+=1
            if a==b:
                b+=1
        else:
            b+=1
print(min_v)