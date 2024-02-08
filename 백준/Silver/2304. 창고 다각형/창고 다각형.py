# 창고 다각형
import sys
input = sys.stdin.readline

def selection_sort(arr,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx]>arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

n = int(input())        # 기둥의 개수
storage_list = []

for _ in range(n):
    L,H = map(int,input().rstrip('\n').split())
    storage_list.append([L,H])
selection_sort(storage_list,n)                  # 기둥 위치 순으로 정렬
Max_H = storage_list[0][1]                      # 첫번째 max
Max_idx = storage_list[0][0]
for k in range(len(storage_list)):
    if Max_H<storage_list[k][1]:
        Max_H = storage_list[k][1]              # 최대값 갱신
        Max_idx = storage_list[k][0]
roof_list = [0]*(storage_list[-1][0]+1)  # 루프 배열
new_storage1 = storage_list[0][1]
for i in range(Max_idx):
    for j in range(len(storage_list)):
        if i >= storage_list[j][0]:
            roof_list[i] = new_storage1
            if new_storage1<storage_list[j][1]:
                new_storage1 = storage_list[j][1]
                roof_list[i] = new_storage1


new_storage2 = storage_list[-1][1]
for k in range(storage_list[-1][0],Max_idx,-1):
    for j in range(len(storage_list)):
        if k <=storage_list[j][0]:
            roof_list[k] = new_storage2
            if new_storage2<storage_list[j][1]:
                new_storage2 = storage_list[j][1]
                roof_list[k] = new_storage2
roof_list[Max_idx] = Max_H
Sum = 0
for l in roof_list:
    Sum+=l
print(Sum)