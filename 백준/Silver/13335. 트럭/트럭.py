# 트럭
from collections import deque
import sys
input = sys.stdin.readline
n,w,L = map(int,input().strip().split())
truck = deque(map(int,input().strip().split()))
bridge = deque([0])*w
t = 1
lst = truck[-1]
fir = truck.popleft()
bridge[0] = fir
while True:
    if bridge[-1] != 0:
        bridge[-1] = 0
    if not truck and sum(bridge)==0:
        break
    if not truck:
        bridge.rotate(1)
    else:
        k = truck[0]
        if k+sum(bridge)>L:
            bridge.rotate(1)
        else:
            i = truck.popleft()
            bridge.rotate(1)
            bridge[0]=i
    t+=1
print(t+1)
