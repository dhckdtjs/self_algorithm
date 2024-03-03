# 팩토리얼 0의 개수
n = int(input())
num_list = [i for i in range(1,n+1)]
cnt = 0
res = 1
for k in num_list:
    if k%5 !=0:
        continue
    while k>0:
        k =  k//5
        cnt+=1
        if k %5 !=0:
            break
print(cnt)
