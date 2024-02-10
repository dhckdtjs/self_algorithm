# 2xn 타일링 2
# 1x2,2x1 & 2x2 타일로 채우는 방법의 수
def tailing(n):
    arr = [0]*(n+1)
    arr[0] = 1
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1]+arr[i-2]*2
    return arr[-1]

n = int(input())
print(tailing(n)%10007)