n,m = list(map(int,input().split()))
lst = []
for i in range(2,n+1):
    lst.append(i)           # 일단 새로운 리스트에 나열

new_list = []               # 빈 리스트 선언 후에 이중 for문을 통해 빼낸 순서로 일단 넣기
for j in range(2,n+1):
    for k in lst:
        if k % j == 0:
            new_list.append(k)

jjin_new_list = []          # 최종 리스트 선언 후에 중복 되는 값 빼내기
for l in new_list:
    if l not in jjin_new_list:
        jjin_new_list.append(l)

print(jjin_new_list[m-1])      # 원하는 값 출력