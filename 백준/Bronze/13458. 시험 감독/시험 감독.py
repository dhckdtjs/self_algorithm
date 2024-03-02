# 시험 감독
# 총 감독관은 한명씩 있어야 함
N = int(input())            # 시험장 개수
A = list(map(int,input().split()))            # 응시자 수
B,C = map(int,input().split()) # 총 감독관 감시자 수, 부 감독관 감시자 수
cnt=len(A)
for i in range(N):
    room = A[i]
    if B>=room:
        continue
    elif B<room:
        room = room-B
        if room<=C:
            cnt+=1
        else:
            res = room//C
            if room%C != 0:
                res+=1
            cnt+=res 
print(cnt)
    