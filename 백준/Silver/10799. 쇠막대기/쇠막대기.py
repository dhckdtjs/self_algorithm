# 쇠막대기
stick = input()
stack = []
cnt = 0
for i in range(len(stick)-1):
    if stick[i] == '(':
        if stick[i+1] == ')':
            cnt+=len(stack)
        else:
            stack.append(stick[i])
    if stick[i] == ')':
        if stick[i+1] == ')':
            cnt+=1
            stack.pop()
print(cnt)