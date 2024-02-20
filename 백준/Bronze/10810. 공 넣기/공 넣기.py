# 공 넣기
N,M = map(int,input().split())
basket = [0]*(N+1)
for _ in range(M):
    i,j,k = map(int,input().split())
    for num in range(i,j+1):
        basket[num] = k
basket.pop(0)
print(*basket)