# ACM 호텔
T = int(input())
for _ in range(T):
    room_list = []
    H,W,n = list(map(int,input().split()))
    for k in range(1,W+1):
        for j in range(1,H+1):
            if k <10:
                room = f'{j}0'+f'{k}'
                room_list.append(room)
            else:
                room = f'{j}'+f'{k}'
                room_list.append(room)

    print(room_list[n-1])
    