# 부분수열의 합

def powerset(idx):
    sm = 0
    res = 0
    global cnt
    if idx == n:
        for i in range(n):
            if c[i]:
                sm+=num[i]
                res+=1
        if res !=0 and sm==s:
            cnt+=1
        return
    c[idx] = 0
    powerset(idx+1)
    c[idx] = 1
    powerset(idx+1)

import sys
input = sys.stdin.readline
n,s = map(int,input().strip().split())
num = list(map(int,input().strip().split()))
c = [i for i in range(n)]
cnt = 0
powerset(0)
print(cnt)