# 괄호
# 올바른 괄호이면 YES, 아니면 NO
n = int(input())

for _ in range(n):
    stack = []
    PS = list(map(str,input().rstrip('\n')))
    for k in PS:
        if len(stack) == 0:
            if k ==')':
                result = False
                break
            elif k == '(':
                stack.append(k)
        else:
            if k == '(':
                stack.append(k)
            elif k == ')':
                stack.pop()
        result = True
    if len(stack) == 0 and result == True:
        print('YES')
    else:
        print('NO')