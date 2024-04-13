# 쿼드 트리
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(input().strip()) for _ in range(n)]
def dfs(i,fr,fc):
    global res
    fir = arr[fr][fc]
    for r in range(fr,fr+i):
        for c in range(fc,fc+i):
            if arr[r][c]!=fir:
                res += '('
                dfs(i//2,fr,fc)
                dfs(i//2,fr,fc+i//2)
                dfs(i//2,fr+i//2,fc)
                dfs(i//2,fr+i//2,fc+i//2)
                res+=')'
                return res
    res+=fir

    return res



res = ''
ans =dfs(n,0,0)
print(ans)