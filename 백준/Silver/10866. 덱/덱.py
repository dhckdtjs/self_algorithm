# 덱
from collections import deque
d = deque()
n = int(input())
deque_list = []
for k in range(n):
    deque_word = input()
    deque_list.append(deque_word)
for i in deque_list:
    try:    
        if 'push' in i:
            num = i.split(' ')[1]
            if 'push_back' in i:
                d.append(num)
            elif 'push_front' in i:
                d.appendleft(num)
        elif i == 'front':
            print(d[0])
        elif i == 'back':
            print(d[-1])
        elif i == 'size':
            print(len(d))
        elif i == 'empty':
            if len(d) == 0:
                print(1)
            else:
                print(0)
        elif i == 'pop_front':
            item = d.popleft()
            print(item)
        elif i == 'pop_back':
            item = d.pop()
            print(item)
        
    except:
        if len(d) == 0:
            print(-1)