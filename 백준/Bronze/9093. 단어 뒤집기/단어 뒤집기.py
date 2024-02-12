# 단어 뒤집기
# 문장이 주어지면 단어를 모두 뒤집어서 출력
n = int(input())
for _ in range(n):
    res = []
    sen = list(map(str,input().split()))
    for k in sen:
        k = k[::-1]
        res.append(k)
    print(*res)