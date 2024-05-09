# 인사성 밝은 곰곰이
n = int(input())
enter = set()
total = 0
for i in range(n):
    word = input()
    if word == 'ENTER':
        total+=len(enter)
        enter = set()
    else:
        if word not in enter:
            enter.add(word)
total+=len(enter)
print(total)