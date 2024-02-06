# 소수 구하기
# M 이상 N 이하의 소수 구해서 하나씩 출력
def is_prime(num):
    if num == 1:
        return False
    for i in range(2,int((num)**(1/2))+1):
        if num% i == 0:
            return False
    return True


num1,num2 = map(int,input().split())
num_list = []
sort_list = []
for i in range(num1,num2+1):
    num_list.append(i)
for k in num_list:
    if is_prime(k) == True:
        sort_list.append(k)
for j in sort_list:
    print(j)
    