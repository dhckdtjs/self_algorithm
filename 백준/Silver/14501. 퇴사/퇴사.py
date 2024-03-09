n = int(input())
day_list = [0]*n
money_list = [0]*n

def dfs(i,sm):
    global max_v
    if i>=n:
        max_v = max(max_v,sm)
        return
    if i+day_list[i]<=n:
        dfs(i+day_list[i],sm+money_list[i])
    dfs(i+1,sm)

for i in range(n):
    day_list[i],money_list[i] = map(int,input().split())
max_v = -float('inf')
dfs(0,0)
print(max_v)