while True:
    sen = str(input())
    stack = []
    flag = True
    if sen=='.':
        break
    try:
        for word in sen:
            if len(stack) == 0:
                if word == ')' or word ==']':
                    flag = False
                    break
            if word == '(' or word =='[':
                stack.append(word)
            if word == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
                    break
            elif word == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
                    break
        if len(stack) == 0 and sen[-1] == '.' and flag !=False:
            print('yes')
        elif flag == False or sen[-1] !='.' or len(stack)!=0:
            print('no')
    except IndexError:
        print('no')