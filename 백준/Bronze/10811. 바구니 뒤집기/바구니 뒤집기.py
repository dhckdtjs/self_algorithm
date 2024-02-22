# 바구니 뒤집기
n,m = map(int,input().split())
basket = [i for i in range(1,n+1)]
for k in range(m):
    start,end = map(int,input().split())
    for j in range((end-start+1)//2):                # 1~2
        tmp = basket[start-1+j]                         # 0,1
        basket[start-1+j] =basket[end-j-1]              # 3,2
        basket[end-j-1] = tmp
print(*basket) 