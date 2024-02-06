# 요세푸스 문제
# 1번부터 N번까지 원을 이룸
# K번째 사람 제거 하고 남은 사람들로 이루어진 원으로 과정 계속 진행
# N명의 사람이 모두 제거될 때까지 계속됨
# 덱을 사용해서 풀어보자(feat.rotation)
from collections import deque
people = deque()
kill_list = []
N,K = map(int,input().split())
for i in range(1,N+1):
    people.append(i)

for _ in range(N):
    people.rotate(-(K-1))
    person = people.popleft()
    kill_list.append(person)
print('<',end='')
k = len(kill_list)
while k>0:
    print(kill_list[N-k],end='')
    k-=1
    if k== 0:
        break
    print(',', end=' ')
print('>')