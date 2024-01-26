T = int(input())
for _ in range(T):
    result = 0
    lst = []
    quiz = input()
    for i in quiz:
        if i == 'O':
            lst.append(i)
            result +=lst.count('O')
        if i == 'X':
            lst = []

    print(result)