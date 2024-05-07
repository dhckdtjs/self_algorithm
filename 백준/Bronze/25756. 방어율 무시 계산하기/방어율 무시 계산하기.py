# 방어율 무시 계산하기ㅣ
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    if i == 0:
        temp = 1-(1-0)*(1-a[i]*0.01)
        v = temp
        print(round(temp*100,6))
    else:
        v= 1-(1-v)*(1-a[i]*0.01)
        print(round(v*100,6))