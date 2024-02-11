# 수 묶기
# N인 수열 주어졌을 때 수열의 합
# 적절히 묶어서 그 합이 최대가 나와야함
# 0, 음수는 같이 묶고 양수는 최대한 큰 거 위주로 묶기
import sys
input = sys.stdin.readline
n = int(input())
num_lst = []
for _ in range(n):
    num = int(input())
    num_lst.append(num)
pls_list = []
mandz_list =[]
for i in num_lst:
    if i>0:
        pls_list.append(i)
    else:
        mandz_list.append(i)
pls_list.sort(reverse=True)
p_sum = 0
m_sum = 0
len_p= len(pls_list)
if len_p%2 == 0:                    # 양수 리스트 길이가 짝수일 경우
    for j in range(0,len_p,2):
        res_p=0
        res_p=pls_list[j]*pls_list[j+1]
        if res_p<pls_list[j]+pls_list[j+1]:
            res_p = pls_list[j]+pls_list[j+1]
        p_sum+=res_p
elif len_p%2 != 0:
    if len_p == 1:
        p_sum = pls_list[0]
    else:
        for k in range(0,len_p-1,2):        # 양수 리스트 길이가 홀수일 경우
            res_p = 0
            res_p=pls_list[k]*pls_list[k+1]
            if res_p < pls_list[k]+pls_list[k+1]:
                res_p = pls_list[k]+pls_list[k+1]
            p_sum+=res_p
        p_sum += pls_list[-1]

len_m = len(mandz_list)
mandz_list.sort()
if len_m%2 == 0:                    # 음수 리스트 길이가 짝수일 경우
    for j in range(0,len_m,2):
        res_m = 0
        res_m=mandz_list[j]*mandz_list[j+1]
        if res_m<mandz_list[j]+mandz_list[j+1]:
            res_m = mandz_list[j]+mandz_list[j+1]
        m_sum+=res_m
elif len_m%2 != 0:
    if len_m == 1:
        m_sum = mandz_list[0]
    else:
        for k in range(0,len_m-1,2):        # 음수 리스트 길이가 홀수일 경우
            res_m = 0
            res_m=mandz_list[k]*mandz_list[k+1]
            if res_m < mandz_list[k]+mandz_list[k+1]:
                res_m = mandz_list[k]+mandz_list[k+1]
            m_sum+=res_m
        m_sum += mandz_list[-1]
res = p_sum+m_sum
print(res)