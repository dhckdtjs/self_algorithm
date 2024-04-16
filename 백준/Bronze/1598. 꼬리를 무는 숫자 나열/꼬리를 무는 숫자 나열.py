# 꼬리를 무는 숫자 나열
n,m = map(int,input().split())
if n % 4== 0:
    a,b = n//4-1,4
else:
    a,b = divmod(n,4)
if m%4 == 0:
    c,d = m//4-1,4
else:
    c,d = divmod(m,4)
# print(a,b)
# print(c,d)
print(abs(c-a)+abs(d-b))