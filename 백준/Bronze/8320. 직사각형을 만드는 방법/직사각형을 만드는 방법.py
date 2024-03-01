n = int(input())
num = 0
for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1): # i의 제곱근까지만 반복
        if i % j == 0:
            if i // j == j: # 정사각형인 경우 (가로와 세로 길이가 같음)
                num += 1
            else: # 직사각형이 회전했을 때 동일하지 않은 경우
                num += 1 # 가로x세로, 세로x가로 두 가지 경우 고려
print(num)
