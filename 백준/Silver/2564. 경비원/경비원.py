# 경비원
# 첫째 수 : 상점 위치 방향 (1,2,: 북남 3,4: 서동)
# 둘째 수 1,2일 경우 왼쪽 경계부터 거리, 3,4일 4경우 위쪽 경계부터 거리

def min_res(n1,n2):
    if n1<n2:
        result = n1
    else:
        result = n2
    return result

def dis_cal(direct,distance):
    if dong_dir == direct:                  # 같은 방향에 존재
        result = abs(dong_dis-distance)
        result_list.append(result)
    elif (direct ==1 and dong_dir == 2) or (direct ==2 and dong_dir == 1)  :         # 반대 방향
        num1 = dong_dis+h+distance
        num2 = (w-dong_dis)+h+(w-distance)
        res1 = min_res(num1,num2)
        result_list.append(res1)
    elif (dong_dir == 3 and direct == 4) or (direct == 3 and dong_dir == 4):
        num1 = dong_dis+w+distance
        num2 = (h-dong_dis)+w+(h-distance)
        res2 = min_res(num1,num2)
        result_list.append(res2)
    else:                                   # 비슷한 방향
        if dong_dir == 1 :
            if direct == 3:
                result2 = distance+dong_dis
            elif direct == 4:
                result2 = (w-dong_dis)+distance
            result_list.append(result2)
        elif dong_dir == 2:
            if direct == 3:
                result3 = dong_dis+(h-distance)
            elif direct == 4:
                result3 = (w-dong_dis)+(h-distance)
            result_list.append(result3)
        elif dong_dir == 3:
            if direct == 1:
                result4 = dong_dis+distance
            elif direct == 2:
                result4 = (h-dong_dis)+distance
            result_list.append(result4)
        else:
            if direct == 1:
                result5 = dong_dis+(w-distance)
            elif direct == 2:
                result5 = (h-dong_dis)+(w-distance)
            result_list.append(result5)
    return result_list
import sys
input = sys.stdin.readline
w,h = map(int,input().split())      # 블록 size
n = int(input())                    # 상점의 개수
dir_list = []
dis_list = []
result_list = []
Sum = 0
for store in range(n):
    direct, distance = map(int,input().split())
    dir_list.append(direct)
    dis_list.append(distance)
dong_dir,dong_dis = map(int,input().split())
for k in range(n):
    total = dis_cal(dir_list[k],dis_list[k])
for num in total:
    Sum+=num
print(Sum)