# 대지
n = int(input())
x_list = set()
y_list = set()
for _ in range(n):
    x,y = map(int,input().split())
    x_list.add(x)
    y_list.add(y)
if n == 1:
    print(0)
else:
    x_max = max(x_list)
    x_min = min(x_list)
    y_max = max(y_list)
    y_min = min(y_list)
    print((x_max-x_min)*(y_max-y_min))