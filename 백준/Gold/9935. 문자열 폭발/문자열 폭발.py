# 문자열 폭발

def check_bomb():
    stack = []
    for ch in sen:
        stack.append(ch)
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
    return stack
sen = str(input())
bomb = str(input())
n = len(bomb)
m = len(sen)
res = check_bomb()
if len(res) == 0:
    print('FRULA')
else:
    for k in res:
        print(k,end='')