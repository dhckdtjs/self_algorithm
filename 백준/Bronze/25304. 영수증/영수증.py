# 영수증
total = int(input())
n = int(input())
s = 0
for _ in range(n):
    price,num = map(int,input().split())
    s+=price*num
if s == total:
    print('Yes')
else:
    print('No')