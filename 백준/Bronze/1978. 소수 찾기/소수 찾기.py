# 소수 찾기
n = int(input())
num_list = list(map(int,input().split()))
prime = 0
for num in num_list:
    for k in range(2,num+1):
        if num%k == 0:
            if k==num:
                prime+=1
            break
print(prime)