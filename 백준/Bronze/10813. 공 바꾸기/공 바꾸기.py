# 공 바꾸기
N,M = map(int,input().split())
basket = [i for i in range(1,N+1)]  # 1 2 3 4 5 
for j in range(M):
    num1,num2 = map(int,input().split())
    temp = basket[num2-1]
    basket[num2-1] = basket[num1-1]
    basket[num1-1] = temp
print(*basket)