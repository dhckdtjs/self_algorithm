# 분해합
n = int(input())
flag = False
for i in range(1,n+1):
    num_list = [i]
    char =str(i)
    for j in char:
        num_list.append(int(j))
    if sum(num_list) == n:
        print(char)
        flag = True
        break
if flag == False:
    print(0)