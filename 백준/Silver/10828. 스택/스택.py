# 스택
N = int(input())
stack_list = []
stack = []
for i in range(N):
    stack_w = input()
    stack_list.append(stack_w)
for k in stack_list:
    if 'push' in k:
        num =int(k.split(' ')[1])
        stack.append(num)
    elif k == 'top':
        try:
            print(stack[-1])
        except:
            if len(stack) == 0:
                print(-1)
    elif k == 'size':
        print(len(stack))
    elif k == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif k == 'pop':
        try:
            item = stack.pop()
            print(item)
        except:
            if len(stack) == 0:
                print(-1)