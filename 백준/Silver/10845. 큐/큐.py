# 큐
que_list = []
stack = []
n = int(input())
for _ in range(n):
    que_w = input()
    que_list.append(que_w)
for k in que_list:
    try:
        if 'push' in k:
            num = k.split(' ')[1]
            stack.append(num)
        elif k =='front':
            print(stack[0])
        elif k == 'back':
            print(stack[-1])
        elif k == 'size':
            print(len(stack))
        elif k == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif k == 'pop':
            item = stack.pop(0)
            print(item)
    except:
            if len(stack) == 0:
                print(-1)