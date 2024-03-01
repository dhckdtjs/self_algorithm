per_list = []
for _ in range(9):
    person = int(input())
    per_list.append(person)
per_list.sort()
n = len(per_list)
total = sum(per_list) - 100
for i in range(n-1):
    for j in range(i+1,n):
        if per_list[i]+per_list[j] == total:
            rm1 = (per_list[i])
            rm2 = (per_list[j])
for k in per_list:
    if k != rm1 and k != rm2:
        print(k)