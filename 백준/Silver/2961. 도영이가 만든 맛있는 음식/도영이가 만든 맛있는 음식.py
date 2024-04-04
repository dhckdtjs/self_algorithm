# 도영이가 만든 맛있는 음식
import sys
input = sys.stdin.readline
n = int(input())

def powerset(idx):
    global min_v
    sm_s = 1
    sm_b = 0
    res = 0
    if idx == n:
        for i in range(n):
            if c[i]:
                sm_s*=food[i][0]
                sm_b+=food[i][1]
                res+=1
        temp=sm_s-sm_b
        temp = abs(temp)
        if min_v<temp:
            return
        if res!=0:
            min_v = min(temp,min_v)
        return
    c[idx] = 0
    powerset(idx+1)
    c[idx] = 1
    powerset(idx+1)

food = []
for i in range(n):
    s,b = map(int,input().split())
    food.append([s,b])
c = [i for i in range(n)]
min_v = float('inf')
powerset(0)
print(min_v)