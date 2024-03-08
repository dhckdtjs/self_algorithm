# 집합
import sys
input = sys.stdin.readline
M = int(input())
S = set()
def action_set(action,x):
    global S
    if action == 'add':
        S.add(int(x))
    elif action == 'remove':
        S.discard(int(x))
    elif action == 'check':
        if int(x) in S:
            print(1)
            return
        else:
            print(0)
            return
    elif action == 'toggle':
        if int(x) in S:
            S.remove(int(x))
        else:
            S.add(int(x))
    elif action == 'all':
        S = set(i for i in range(1,21))
    elif action =='empty':
        S = set()

for _ in range(M):
    action = (input().split())
    if len(action) == 1:
        action.append(0)
        do,num = action[0],action[1]
    else:
        do,num = action[0],action[1]
    action_set(do,num)