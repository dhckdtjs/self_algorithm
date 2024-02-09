# 수 찾기
# 정수 주어졌을 때, 이 안에 X라는 정수가 존재하는지 알아내기
n = int(input())
num_list = list(map(int,input().split()))
m = int(input())
check_list = list(map(int,input().split()))
dic ={}
for k in num_list:
    if k in dic:
        dic[k]+=1
    else:
        dic[k] = 1
for j in check_list:
    if j in dic:
        print(1)
    else:
        print(0)