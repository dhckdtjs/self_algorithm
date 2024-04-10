# 기타 레슨
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
lecture = list(map(int,input().strip().split()))

start = max(lecture)
end = sum(lecture)
ans = end
while start<=end:
    mid = (start+end)//2
    total = 0
    cnt = 1
    for k in lecture:
        if total+k>mid:
            cnt+=1
            total = 0
        total+=k
        # print(total,mid)
    if cnt ==m:
        ans = mid
        end = mid - 1
    elif cnt>m:
        start = mid+1
    else:
        ans = mid
        end = mid-1

print(ans)


