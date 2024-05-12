# 연산자 끼워넣기
n = int(input())

def dfs(i,s,add,minus,mul,div):
    global min_v
    global max_v
    if i == n-1:
        if min_v >s:
            min_v = s
        if max_v<s:
            max_v = s
        return
    if add >0:
        dfs(i+1,s+num[i+1],add-1,minus,mul,div)
    if minus>0:
        dfs(i+1,s-num[i+1],add,minus-1,mul,div)
    if mul>0:
        dfs(i+1,s*num[i+1],add,minus,mul-1,div)
    if div>0:
        if s<0:
            dfs(i+1,-(-s//(num[i+1])),add,minus,mul,div-1)
        else:
            dfs(i+1,s//num[i+1],add,minus,mul,div-1)


num = list(map(int,input().split()))
add,minus,mul,div = map(int,input().split())
min_v = float('inf')
max_v = -float('inf')
dfs(0,num[0],add,minus,mul,div)
print(max_v)
print(min_v)