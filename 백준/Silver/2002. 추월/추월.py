# 추월
n = int(input())
enter = []
out = []
for i in range(n):
    car = input()
    enter.append(car)
for j in range(n):
    o_car = input()
    out.append(o_car)
enter_index = {}
for idx, car in enumerate(enter):
    enter_index[car] = idx
out_order = []
for car in out:
    out_order.append(enter_index[car])
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if out_order[i]> out_order[j]:
            cnt+=1
            break
print(cnt)