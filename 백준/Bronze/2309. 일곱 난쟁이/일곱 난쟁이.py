# 일곱 난쟁이
# 9명이 주어지고 합이 100인 7명 찾기 후 오름차순 정렬
# 안되는 경우 없음
def selection_sort(arr,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx]>arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr


def powerset(idx):
    s = 0
    global result
    if idx == N:
        res = []
        for k in range(N):
            if c[k]:
                s+=little_list[k]
                res.append(little_list[k])
            if s>100:
                break
        if s == 100 and len(res) == 7:
            result = res
        return
    c[idx] = 0
    powerset(idx+1)
    c[idx] = 1
    powerset(idx+1)
            


little_list = []
for p in range(9):
    p = int(input())
    little_list.append(p)
selection_sort(little_list,9)   # 정렬
N = 9
c=[0]*N
powerset(0)
for person in result:
    print(person)