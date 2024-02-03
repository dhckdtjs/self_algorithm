# 스위치 켜고 끄기
n = int(input())                        # n받기
switch = list(map(int,input().split())) # 스위치 배열
student = int(input())                  # 학생 수
def change(arr,num):
    if arr[num] ==1:
        arr[num] = 0
    elif arr[num] == 0:
        arr[num] =1
    return arr[num]
for _ in range(student):
    gen,num = map(int,input().split())  # 성별, 받은 수
    if gen == 1:                        # 남자 =1
        if num == 1:
            for h in range(n):
                change(switch,h)
        else:
            for i in range(1,n+1):
                if i % num == 0:
                    change(switch,i-1)
    elif gen == 2:
        change(switch,num-1)
        if n-num>num:
            min = num
        else:
            min = n-num+1
        for j in range(1,min):
            if switch[num-j-1] == switch[num+j-1] :  # 스위치 양 쪽 같으면
                change(switch, num-j-1)
                change(switch, num+j-1)
            else:
                break
for k in range(1,n+1):
    print(switch[k-1],end=' ')
    if k % 20 == 0:
        print()
