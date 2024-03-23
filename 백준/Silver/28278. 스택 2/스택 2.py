# 스택 2
import sys
input = sys.stdin.readline
n = int(input())
stack= []
def check_stack(a,e):
    if a == 1:
        stack.append(e)
    elif a == 2:
        if len(stack)==0:
            print(-1)
        else:
            k = stack.pop()
            print(k)
    elif a==3:
        print(len(stack))
    elif a==4:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])


for _ in range(n):
    num = input().split()
    if len(num) == 1:
        act = int(num[0])
        number = 0
    else:
        act = int(num[0])
        number = int(num[1])
    check_stack(act,number)