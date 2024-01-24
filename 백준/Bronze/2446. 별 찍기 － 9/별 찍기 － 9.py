# 별 찍기 - 9
n = int(input())
for i in range(1,n+1):
    print(' '*(i-1)+'*'*(2*(n-i+1)-1))
for k in range(1,n):
    print(' '*(n-k-1)+'*'*(2*k+1))