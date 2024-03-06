# 랜선 자르기
K,N = map(int,input().split())
lan_list = [int(input()) for _ in range(K)]
start = 1
end =max(lan_list)
ans = 0
while start<=end:
    res = 0
    mid = (start+end)//2
    for k in lan_list:
        res += k//mid
    if res >= N:
        ans = max(mid,ans)
        start = mid+1
    else:
        end = mid-1
print(ans)