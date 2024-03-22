# 베르트랑 공준
import sys
input = sys.stdin.readline
def check_prime(n):
    cnt = 0
    for i in range(n+1,2*n+1):
        if i == 1:
            continue
        for j in range(2,int(i**(1/2))+1):
            if i% j == 0:
                break
        else:
            cnt+=1
    return cnt


while True:
    k = int(input())
    if k == 0:
        break
    else:
        ans = check_prime(k)
        print(ans)