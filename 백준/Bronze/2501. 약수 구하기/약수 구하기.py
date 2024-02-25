# 약수 구하기
num,order = map(int,input().split())
div_list = []

def quick_sort(target):
    N = len(target)
    if N<=1:
        return target
    left = []
    right = []
    p_idx = N//2
    pivot = target[p_idx]
    for idx in range(N):
        if idx == p_idx : continue
        if target[idx]<pivot:
            left.append(target[idx])
        else:
            right.append(target[idx])
    return quick_sort(left)+[pivot]+quick_sort(right)

for i in range(1,int((num)**(0.5))+1):
    if num%i == 0:
        if num//i == i:
            div_list.append(i)
        else:
            div_list.append(i)
            div_list.append(num//i)
res =quick_sort(div_list)
if order>len(res):
    print(0)
else:
    print(res[order-1])