n = int(input())
num = 0
for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1): # i의 제곱근까지만 반복
        if i%j == 0:
            num+=1
print(num)
