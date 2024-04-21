# 나무 자르기
n,m = map(int,input().split())
tree = list(map(int,input().split()))
def dfs(i):
    s= 0
    for t in tree:
        if t-i<=0:
            continue
        s+=t-i
    return s

start = 0
end = max(tree)
while start<=end:
    mid = (start+end)//2
    res = dfs(mid)
    if res<m:
        end = mid-1
    elif res>m:
        start = mid+1
    else:
        print(mid)
        break
else:
    print(end)