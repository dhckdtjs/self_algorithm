# 수열
n = int(input())
num_list = list(map(int,input().split()))
cnt1 = 1
cnt2 = 1
i = 0
Max_cnt = 1
while i<n-1:
    if num_list[i]<=num_list[i+1]:
        cnt1+=1
    elif num_list[i]>num_list[i+1]:
        cnt1=1
    i+=1
    if Max_cnt<cnt1:
        Max_cnt = cnt1

while i>0:
    if num_list[i]<=num_list[i-1]:
        cnt2+=1
    elif num_list[i]>num_list[i-1]:
        cnt2=1
    i-=1
    if Max_cnt<cnt2:
        Max_cnt = cnt2
print(Max_cnt)