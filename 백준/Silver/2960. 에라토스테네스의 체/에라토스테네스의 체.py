n,m = list(map(int,input().split()))
lst = []
for i in range(2,n+1):
    lst.append(i)

new_list = []
for j in range(2,n+1):
    for k in lst:
        if k % j == 0:
            new_list.append(k)

jjin_new_list = []
for l in new_list:
    if l not in jjin_new_list:
        jjin_new_list.append(l)

print(jjin_new_list[m-1])