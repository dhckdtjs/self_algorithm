# 음계
num_list = list(map(int,input().split()))
new_list = []
rv_new = []
for k in num_list:
    new_list.append(k)
new_list.sort()
rv_new = sorted(num_list)
rv_new.reverse()
if num_list == new_list:
    print('ascending')
elif num_list == rv_new:
    print('descending')
else:
    print('mixed')