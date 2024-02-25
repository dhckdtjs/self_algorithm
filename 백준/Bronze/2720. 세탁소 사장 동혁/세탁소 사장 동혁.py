# 세탁소 사장 동혁
n = int(input())
coin_list = [25,10,5,1]
for _ in range(n):
    money = int(input())
    change_list = [0]*4
    k = 0
    while money >=1:
        coin = money//coin_list[k]
        money = money%coin_list[k]
        change_list[k] = coin
        k+=1
    print(*change_list)