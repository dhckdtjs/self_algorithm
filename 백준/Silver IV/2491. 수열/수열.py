# 수열
n = int(input())
num_list = list(map(int,input().split()))
i = 0
cnt1 = 1
cnt2 = 1
Max_cnt1 = 1
Max_cnt2 = 1
Max_res = 0

while i<n-1:
    if num_list[i]<=num_list[i+1]:
        cnt1+=1
    elif num_list[i]>num_list[i+1]:
        cnt1=1
    i+=1
    if Max_cnt1<cnt1:
        Max_cnt1 = cnt1
while i >0:
    if num_list[i]<=num_list[i-1]:
        cnt2+=1
    elif num_list[i]>num_list[i-1]:
        cnt2=1
    i-=1
    if Max_cnt2<cnt2:
        Max_cnt2 = cnt2
if Max_cnt2<Max_cnt1:
    Max_res = Max_cnt1
elif Max_cnt1<Max_cnt2:
    Max_res = Max_cnt2
elif Max_cnt1 == Max_cnt2:
    if len(num_list) == 1:
        Max_res = 1
    else:
        Max_res = Max_cnt1
print(Max_res)