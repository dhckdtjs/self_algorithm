# 최대공약수와 최소공배수
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수 출력
def prime(N,i,arr):
    while N>1:
        if N% i == 0:
            N = N//i
            arr.append(i)
            i=2
        else:
            i+=1
        if N== 1:
            break
    return arr
N,M = map(int,input().split())
N_list = []
M_list = []
i = 2
Max_total = 1
Min_total = 1
prime(N,i,N_list)
prime(M,i,M_list)
Max_list = []
Min_list = []
for k in N_list:
    if k in M_list:
        Max_list.append(k)
        M_list.remove(k)
    else:
        Min_list.append(k)
for j in M_list:
    Min_list.append(j)
for l in Max_list:
    Max_total*=l
for h in Min_list:
    Min_total*=h
print(Max_total)
print(Max_total*Min_total)