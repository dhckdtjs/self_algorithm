# 설탕배달

n = int(input())
for cnt_5 in range(n//5,-1,-1):
    cnt_3 = (n-(5*cnt_5))//3
    if cnt_5*5+cnt_3*3 == n:
        print(cnt_5+cnt_3)
        break
else:
    print(-1)