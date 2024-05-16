# 학식 사주기
n = int(input())
menu = []
for i in range(n):
    meal = int(input())
    menu.append(meal)
m = int(input())
total = 0
for i in range(m):
    want = int(input())
    total+=menu[want-1]
print(total)