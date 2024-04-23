# 투에-모스 문자열

n = int(input())
def dfs(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i%2 == 1:
        return 1-dfs(i//2)
    else:
        return dfs(i//2)
print(dfs(n-1))