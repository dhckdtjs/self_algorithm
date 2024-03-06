# 프린트 큐
from collections import deque
T =int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    print_list = []
    num_list = list(enumerate(map(int,input().split())))
    new_num = sorted(num_list,key=lambda x:x[1],reverse=True)
    new_num = deque(new_num)
    Max_num = new_num[0][1]
    Max_idx = new_num[0][0]

    while new_num:
        if num_list[Max_idx][1] == new_num[0][1]:
            print_list.append(num_list[Max_idx])
            new_num.popleft()
        Max_idx = (Max_idx+1)%N
    for k in range(len(print_list)):
        if M == print_list[k][0]:
            print(k+1)


