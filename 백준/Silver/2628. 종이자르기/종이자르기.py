# 종이 자르기
# 종이 가로 세로
# 점선의 개수
# 0이 가로 1이 세로
# 가장 큰 종이 출력
def bubble_sort(arr,n):
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
paper_h, paper_v =map(int,input().split())
n = int(input())
h_list = []
v_list = []
h_list.append(0)
v_list.append(0)
h_list.append(paper_h)
v_list.append(paper_v)
for _ in range(n):
    cut,place = map(int,input().split())
    if cut == 0:
        v_list.append(place)
    if cut == 1:
        h_list.append(place)
Max_v = 0
Max_h = 0
v_list = bubble_sort(v_list,len(v_list))
h_list = bubble_sort(h_list,len(h_list))
for k in range(1,len(v_list)):
    total_v = v_list[k]-v_list[k-1]
    if Max_v<total_v:
        Max_v = total_v
for h in range(1,len(h_list)):
    total_h = h_list[h]-h_list[h-1]
    if Max_h<total_h:
        Max_h = total_h
print(Max_h*Max_v)