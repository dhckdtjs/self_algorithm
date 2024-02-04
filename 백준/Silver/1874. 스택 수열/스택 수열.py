# 스택 수열
# + = push - = : pop 단 push는 반드시 오름차순
# 스택을 이용해 수열을 만들 수 있는지 없는지?
# 정해져있지 않음 -> while 사용
stack = []
n = int(input())
ans  = []
cnt = 1
result = True
for i in range(n):
    num = int(input())
    while cnt <=num:
        stack.append(cnt)
        cnt+=1
        ans.append('+')
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        result = False
if result == True:
    for k in ans:
        print(k)
else:
    print('NO')