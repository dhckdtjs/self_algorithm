# 알고리즘 수업 - 피보나치 수 1
def fibo(n):
    cnt = 0
    a,b = 1,0
    for i in range(n):
        a,b = b,a+b
    return b

def fibonacci(n):
    DP = [1,1]
    cnt = 0
    for i in range(2,n):
        DP.append(DP[-1]+DP[-2])
        cnt+=1
    return cnt

n = int(input())
print(fibo(n),fibonacci(n))