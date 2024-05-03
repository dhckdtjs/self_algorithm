# 인공지능 시계
a,b,c = map(int,input().split())
d = int(input())
total = a*(60)**2+b*60+c+d
h = total//(60)**2
total = total%(60)**2
m = total//60
total = total%60
s = total%60
if h>=24:
    temp = h//24
    h-=24*temp
    print(h,m,s)
else:
    print(h,m,s)