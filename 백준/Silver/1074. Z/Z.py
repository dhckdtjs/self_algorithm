# Z
import sys
input = sys.stdin.readline
n,r,c = map(int,input().strip().split())
def z(n,r,c,res):
    if n == 0:
        return res
    half = 2 ** (n - 1)

    if r<half and c<half:
        q = 1
    elif r<half and c>=half:
        q= 2
        c-=half
    elif r>=half and c<half:
        q = 3
        r-=half
    else:
        q = 4
        r-=half
        c-=half
    res+=(q-1)*(half)**2
    return z(n-1,r,c,res)
ans = z(n,r,c,0)
print(ans)