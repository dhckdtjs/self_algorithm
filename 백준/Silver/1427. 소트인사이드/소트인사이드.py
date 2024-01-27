# 소트인사이드
num = list(input())
new_list = []
for i in num:
   k = int(i)
   new_list.append(k)
new_list.sort(reverse=True)
for j in new_list:
    print(j,end='')