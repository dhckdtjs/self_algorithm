# 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
multi = str(A*B*C)
for i in range(10):
    print(multi.count(f'{i}'))