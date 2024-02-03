# 카드 2
# 입력 받은 후 제일 위에 카드 제거
# 제일 위에 카드 맨 밑으로
# 반복해서 마지막까지 남은 카드 구하기
from collections import deque

n = int(input())
card = deque()

for i in range(1,n+1):
    card.append(i)
while n>1:
    card.popleft()
    n-=1
    item = card.popleft()
    card.append(item)
print(*card)