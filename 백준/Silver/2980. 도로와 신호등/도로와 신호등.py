# 도로와 신호등
# 빨강이면 기다렸다 출발
N, L = map(int,input().split())     # 신호등 개수 N, 도로의 길이ㅣ L
time = 0
truck = 0
for _ in range(N):
    D,R,G = map(int,input().split())    # D 신호등 위치 , R,G: 빨간색,초록 지속되는 시간
    time += D-truck
    truck = D
    cycle = time % (R+G)
    if cycle<R:
        time += R- cycle
time+=L-truck
print(time)    
