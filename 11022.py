# A+B - 8
n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    print(f'Case #{i+1}: {a} + {b} = {a+b}')