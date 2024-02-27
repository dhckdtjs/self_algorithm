# 달팽이는 올라가고 싶다.
A,B,V =map(int,input().split())
cnt = 1
res = (V-A)/(A-B)
num = int(res)
if res != num:
    res = int(res)+1
else:
    res = int(res)
print(cnt+res)