n , m = list(map(int,input().split()))
s = []
num = list(map(int,input().split()))
num.sort()
def dfs():
    if len(s) == m:
        print(" ".join(map(str,s)))
        return None
    for i in num:
            s.append(i)
            dfs()
            s.pop()
dfs()
