# X보다 작은 수
N,X = list(map(int,input().split()))
num_list = list(map(int,input().split()))
for k in num_list:
    if X>k:
        print(k,end =' ') 