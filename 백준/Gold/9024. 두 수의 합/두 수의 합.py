# 두 수의 합
T = int(input())

def binary_cnt(i):
    global cnt
    global diff
    start = i+1
    end = n - 1
    while start<=end:
        mid = (start+end)//2
        twosum = num_list[i]+num_list[mid]
        if twosum<k:
            start = mid+1
        else:
            end = mid-1
        if abs(twosum-k)<diff:
            diff = abs(twosum-k)
            cnt = 1
        elif abs(twosum-k) == diff:
            cnt+=1

for tc in range(1,T+1):
    n,k = map(int,input().split())
    num_list = list(map(int,input().split()))
    num_list.sort()
    cnt = 0
    diff = float('inf')
    for i in range(n-1):
        binary_cnt(i)
    print(cnt)
