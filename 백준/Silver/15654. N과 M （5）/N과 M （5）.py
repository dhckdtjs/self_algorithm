n,m = map(int,input().split())
s = []
num = list(map(int,input().split()))
num.sort()
def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in num:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()